from db_connect.query import Query
from db_config import DB_Config

class SensorRepository:

    def update(query):
        updated_sensor = Query.update(query)
        return updated_sensor

    def get_sensor_count():
        sql = " SELECT count(id) as count FROM sensors"
        sql += " WHERE sensors.deleted_at is Null"
 
        total_count = Query.select(sql)
        return total_count

    def get_sensor_list(offset, limit):
        sql = " SELECT sensors.* FROM sensors"
        sql += " WHERE sensors.deleted_at is Null"
        sql += " ORDER BY sensors.id DESC"
        sql += " LIMIT %s OFFSET %s" %(limit, offset)
 
        sensor = Query.selectAll(sql)
        return sensor
    
    def get_database_size():

        sql = "SELECT SUM(ROUND(((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024), 2)) AS 'database_size' "
        sql += "FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '%s'" %(DB_Config.db_name)

        table_size = Query.select(sql)
        return table_size