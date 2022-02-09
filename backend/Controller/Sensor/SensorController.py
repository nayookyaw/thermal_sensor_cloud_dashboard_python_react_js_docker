from flask import request, jsonify

from Common.TextConstants import TextConstants
from Services.Logging.LoggingInfo import LoggingInfo

from DAO.Sensor.SensorRepository import SensorRepository

class SensorController:

    def get_sensor_count():
        total_count = SensorRepository.get_sensor_count()

        database_size = SensorRepository.get_database_size()

        res_data = {
            'total_count' : total_count['count'],
            'database_size' : float(database_size['database_size'])
        }
        
        return jsonify({ "status" : TextConstants.GET_SENSOR_COUNT_SUCCESS, "data" : res_data }), 200

    def get_sensor_list():
        data = request.get_json('data')

        offset = data['req_data']['offset']
        limit = data['req_data']['limit']

        sensor = SensorRepository.get_sensor_list(offset, limit)
        
        return jsonify({ "status" : TextConstants.GET_SENSOR_LIST_SUCCESS, "data" : sensor }), 200
    
    def update_sensor_allow():
        data = request.get_json('data')
        sensor_id = data['req_data']['sensor_id']
        is_block_s = data['req_data']['is_allow']

        query = "UPDATE sensors SET is_block = '%s'" %(is_block_s)
        query += " WHERE id = %s" %(sensor_id)

        updated_sensor = SensorRepository.update(query)
        
        return jsonify({ "status" : TextConstants.UPDATE_SENSOR_ALLOW_SUCCESS, "data" : updated_sensor }), 200

        