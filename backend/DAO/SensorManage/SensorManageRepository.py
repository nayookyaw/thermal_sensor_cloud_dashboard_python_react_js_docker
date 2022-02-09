from db_connect.query import Query
from db_config import DB_Config

class SensorManageRepository:

    def save(query):
        save_q = Query.save(query)
        return save_q
        
    def update(query):
        update_q = Query.update(query)
        return update_q

    def get_sensor_manage_s():
        sql = " SELECT sensor_manage.* from sensor_manage"
        sql += " WHERE sensor_manage.deleted_at is Null"
        sql += " ORDER BY sensor_manage.id DESC"
        sql += " LIMIT 1"
 
        status = Query.select(sql)
        return status
