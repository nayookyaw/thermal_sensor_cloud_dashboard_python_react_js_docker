"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from __main__ import db

class SensorManage(db.Model):
  """ Data model for sensor manage """

  __tablename__ = 'sensor_manage'
  
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  auto_sync = db.Column(
    db.Integer,
    index = True,
    unique = False,
    nullable= True,
    default = 0
  )
  block_all_sensor = db.Column(
    db.Integer,
    index = True,
    unique = False,
    nullable= True,
    default = 1
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
      'auto_sync' : self.auto_sync,
      'block_all_sensor' : self.block_all_sensor,
    }

    return res_json

  def __repr__(self):
    return '<SensorManage {}>'.format(self.id)
