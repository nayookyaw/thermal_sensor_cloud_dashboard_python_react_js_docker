"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from Models.Sensor import Sensor
from __main__ import db
from operator import and_, or_

class SensorRepository:

    def save(sensor):
        db.session.add(sensor)
        db.session.commit()
    
    def update():
        db.session.commit()
    
    def getSensorByMacAddress(mac_address):
        filter_group = and_(Sensor.deleted_at.is_(None), Sensor.mac_address == mac_address)
        sensor = Sensor.query.filter(filter_group).first()

        return sensor

