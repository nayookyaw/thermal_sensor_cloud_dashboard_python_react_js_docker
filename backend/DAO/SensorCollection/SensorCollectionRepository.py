from db_connect.query import Query

class SensorCollectionRepository:

    def get_sensor_collection_count(sensor_id):
        sql = " SELECT count(*) as count FROM sensor_collection"
        sql += " WHERE sensor_collection.deleted_at is Null AND sensor_collection.sensor_id = %s " %(sensor_id)
        
        sensor_col = Query.select(sql)
        return sensor_col

    def get_sensor_collection(sensor_id, offset, limit):
        sql = " SELECT sensor_collection.* FROM sensor_collection"
        sql += " WHERE sensor_collection.deleted_at is Null AND sensor_collection.sensor_id = %s " %(sensor_id)
        sql += " ORDER BY sensor_collection.id DESC"
        sql += " LIMIT %s OFFSET %s" %(limit, offset)
        
        sensor_col = Query.selectAll(sql)
        return sensor_col