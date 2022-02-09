from __main__ import db

class Role(db.Model):
  """ Data model for role """

  __tablename__ = 'roles'
  
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  role_name = db.Column(
    db.String(80),
    index = True,
    unique = False,
    nullable= False
  )
  user_creation = db.Column(
    db.Integer,
    index = False,
    unique = False,
    nullable = True
  )
  user_list = db.Column(
    db.Integer,
    index = False,
    unique = False,
    nullable = True
  )
  role_creation = db.Column(
    db.Integer,
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
      'role_name' : self.role_name,
      'role_creation' : self.role_creation,
      'user_creation' : self.user_creation,
      'user_list' : self.user_list,
    }

    return res_json

  def __repr__(self):
    return '<Role {}>'.format(self.role_name)
