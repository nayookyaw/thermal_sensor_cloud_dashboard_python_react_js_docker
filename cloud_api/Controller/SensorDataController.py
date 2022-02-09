"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from Models.Sensor import Sensor
from Models.SensorCollection import SensorCollection

from DAO.Sensor.SensorRepository import SensorRepository
from DAO.SensorCollection.SensorCollectionRepository import SensorCollectionRepository
from DAO.SensorManage.SensorManageRepository import SensorManageRepository


from flask import request, jsonify

from datetime import timedelta
import threading

from Services.Logging.LoggingInfo import LoggingInfo

from Common.TextConstants import TextConstants
from constants import Constants

class SensorDataController:

    def save_sensor():
        try:
            input_req = request.form
            input_dict = input_req.to_dict(flat=False)

            # check the input validation
            if (len(input_dict) <= 0):
                return jsonify({ "status" : TextConstants.INVALID_INPUT}), 200
            
            mac_address = input_dict['mac_address'][0]
            sensor_data_str = input_dict['sensor_data'][0]
            
            if (mac_address and sensor_data_str):
                is_auto_sync = False
                is_block_all = True

                # get sensor manage status
                sensor_manage_status = SensorManageRepository.get_manage_status()
                if sensor_manage_status and sensor_manage_status.id:
                    
                    if sensor_manage_status.auto_sync == 1:
                        is_auto_sync =  True
                    
                    if sensor_manage_status.block_all_sensor == 0:
                        is_block_all = False
                
                existing_sensor = SensorRepository.getSensorByMacAddress(mac_address)

                # check new sensor or old
                if existing_sensor == None:
                    if (is_auto_sync == True):
                        new_sensor = Sensor(
                            mac_address = mac_address,
                            is_block = 1
                        )

                        # save data as new into database
                        SensorRepository.save(new_sensor)
                        LoggingInfo.saveLogging("Added new sensor to database " + str(mac_address))
                
                # existing sensor
                else:
                    # check block is false (meaning allow to save this sensor data)
                    is_allow = int(existing_sensor.is_block)

                    if (is_block_all == False):
                        if ( is_allow == 1):
                            sensor_data = {
                                'sensor_id' : existing_sensor.id,
                                'sensor_data' : sensor_data_str
                            }

                            update_sensor_thread = threading.Thread(target=SensorDataController.addSensorData, args=(sensor_data, ))
                            update_sensor_thread.start()
                
                return jsonify({ "status" : TextConstants.SENSOR_DATA_SAVE_SUCCESS}), 200
            else:
                no_data_m_s = "There is no data for either mac address or sensor data"
                LoggingInfo.saveErrorLogForDeveloper(no_data_m_s)
                return jsonify({ "status" : no_data_m_s }), 400

        except Exception as e:
            LoggingInfo.saveErrorLogForDeveloper(TextConstants.ERR_SAVE_SENSOR_DATA + " " + str(e))
            return jsonify({ "status" : TextConstants.ERR_SAVE_SENSOR_DATA }), 400
    
    def addSensorData(s_data):
        new_s_collection = SensorCollection(
            sensor_id = s_data['sensor_id'],
            sensor_data = s_data['sensor_data']
        )

        SensorCollectionRepository.save(new_s_collection)


        