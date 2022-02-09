"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from __main__ import db

class SensorCollection(db.Model):
  """ Data model for sensor collection"""

  __tablename__ = 'sensor_collection'
  
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  sensor_id = db.Column(
    db.Integer,
    index = True,
    unique = False,
    nullable= False
  )
  sensor_data = db.Column(
    db.String(1500),
    index = False,
    unique = False,
    nullable = True
  )
  updated_at = db.Column(
    db.DateTime,
    index = False,
    unique = False,
    nullable = True
  )
  created_at = db.Column(
    db.DateTime,
    index = False,
    unique = False,
    nullable = True,
    default = db.func.current_timestamp()
  )
  deleted_at = db.Column(
    db.DateTime,
    index = False,
    unique = False,
    nullable = True
  )

  def to_json(self):
    res_json = {
      'id' : self.id,
      'sensor_id' : self.sensor_id,
      'sensor_data' : self.sensor_data,
    }

    return res_json

  def __repr__(self):
    return '<Sensor Collection {}>'.format(self.id)
