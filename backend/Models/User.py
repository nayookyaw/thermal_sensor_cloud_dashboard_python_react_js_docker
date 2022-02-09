from __main__ import db

""" phyo import """
import flask_login

class User(db.Model, flask_login.UserMixin):
  """ Data model for user """

  __tablename__ = 'users'
  
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
  email = db.Column(
    db.String(120),
    index = True,
    unique = False,
    nullable = False
  )
  password = db.Column(
    db.String(180),
    index = False,
    unique = False,
    nullable = False
  )
  phone = db.Column(
    db.String(80),
    index = True,
    unique = False,
    nullable = True
  )
  role_id = db.Column(
    db.String(64),
    index = False,
    unique = False,
    nullable = True
  )
  user_type = db.Column(
    db.String(64),
    index = False,
    unique = False,
    nullable = True
  )
  token = db.Column(
    db.String(180),
    index = False,
    unique = False,
    nullable = True
  )
  forgot_password_token = db.Column(
    db.String(180),
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
      'email' : self.email,
      'phone' : self.phone,
      'role_id' : self.role_id,
    }

    return res_json

  def __repr__(self):
    return '<User {}>'.format(self.username)
