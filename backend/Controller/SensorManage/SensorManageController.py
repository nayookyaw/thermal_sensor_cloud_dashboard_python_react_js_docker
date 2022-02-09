from flask import request, jsonify

from datetime import datetime

from Common.TextConstants import TextConstants
from Services.Logging.LoggingInfo import LoggingInfo

from DAO.SensorManage.SensorManageRepository import SensorManageRepository

class SensorManageController:

    def get_sensor_manage_status():
        manage_status = []

        manage_status = SensorManageRepository.get_sensor_manage_s()
        if (manage_status):
            manage_status = manage_status
        
        return jsonify({ "status" : TextConstants.GET_SENSOR_MANAGE_SUCCESS, "data" : manage_status }), 200

    def update_sensor_manage_status():
        data = request.get_json('data')

        type = data['req_data']['type']
        value = int(data['req_data']['value'])

        edit_column = None
        if type == "sync":
            edit_column = "auto_sync"
        elif type == "block":
            edit_column = "block_all_sensor"

        now_date = datetime.now()
        now_str = now_date.strftime("%Y-%m-%d %H:%M:%S")

        manage_status = SensorManageRepository.get_sensor_manage_s()
        
        if edit_column != None:
            if (manage_status and manage_status['id']):
                query = "UPDATE sensor_manage SET %s = %s, " % (edit_column, value)
                query += " updated_at = '%s'" % (now_str)
                query += " WHERE id = '%s'" % (manage_status['id'])

                update_status = SensorManageRepository.update(query)
            else:
                sync_val = None
                block_val = None

                # block is 1 as default / sync is 0 as default
                if edit_column == "auto_sync":
                    sync_val = value
                    block_val = 1
                elif edit_column == "block_all_sensor":
                    sync_val = 0
                    block_val = value
                
                query = "INSERT INTO sensor_manage (auto_sync, block_all_sensor, created_at) VALUES (%s, %s, '%s')" %(sync_val, block_val, now_str)
                saved_s = SensorManageRepository.save(query)

        return jsonify({ "status" : TextConstants.UPDATE_SENSOR_MANAGE_SUCCESS, "data" : "test" }), 200
