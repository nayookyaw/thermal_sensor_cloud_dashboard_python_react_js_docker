from __main__ import db

class AuthToken(db.Model):
  """ Data model for auth token """

  __tablename__ = 'auth_token'
  
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  username = db.Column(
    db.String(80),
    index = True,
    unique = False,
    nullable= False
  )
  refresh_token = db.Column(
    db.String(150),
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
      'username' : self.username,
    }

    return res_json

  def __repr__(self):
    return '<AuthToken {}>'.format(self.id)
