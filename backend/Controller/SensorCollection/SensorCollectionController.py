from flask import request, jsonify

from Common.TextConstants import TextConstants
from Services.Logging.LoggingInfo import LoggingInfo

from DAO.SensorCollection.SensorCollectionRepository import SensorCollectionRepository

class SensorCollectionController:

    def get_sensor_collection_count():
        try:
            data = request.get_json('data')
            sensor_id = data['req_data']['sensor_id']

            temp_sensor_col_count = SensorCollectionRepository.get_sensor_collection_count(sensor_id)
            sensor_col_count = temp_sensor_col_count['count']

            return jsonify({ "status" : TextConstants.GET_SENSOR_COLLECTION_COUNT_SUCCESS, "data" : sensor_col_count }), 200
        except Exception as err:
            return jsonify({ "status" : str(err) }), 400

    def get_sensor_collection():
        try:
            data = request.get_json('data')
            sensor_id = data['req_data']['sensor_id']
            offset = data['req_data']['offset']
            limit = data['req_data']['limit']

            sensor_coll = SensorCollectionRepository.get_sensor_collection(sensor_id, offset, limit)

            return jsonify({ "status" : TextConstants.GET_SENSOR_COLLECTION_SUCCESS, "data" : sensor_coll }), 200
        except Exception as err:
            return jsonify({ "status" : str(err) }), 400
