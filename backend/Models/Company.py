from __main__ import db

class Company(db.Model):
  """ Data model for company """

  __tablename__ = 'company'
  
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  name = db.Column(
    db.String(80),
    index = True,
    unique = False,
    nullable= False
  )
  remark = db.Column(
    db.String(150),
    index = False,
    unique = False,
    nullable = True
  )
  company_token = db.Column(
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
      'name' : self.name,
      'remark' : self.remark,
      'company_token' : self.company_token,
    }

    return res_json

  def __repr__(self):
    return '<AuthToken {}>'.format(self.id)
