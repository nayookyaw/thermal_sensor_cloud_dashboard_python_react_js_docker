"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from Models.SensorCollection import SensorCollection
from __main__ import db
from operator import and_, or_

class SensorCollectionRepository:

    def save(sensor_collection):
        db.session.add(sensor_collection)
        db.session.commit()
    
    def update():
        db.session.commit()


