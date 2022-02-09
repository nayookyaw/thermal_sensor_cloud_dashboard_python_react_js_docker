from __main__ import db
from datetime import datetime
from Models.User import User
from Models.Role import Role

from flask import jsonify

from DAO.User.UserRepository import UserRepository
from DAO.Role.RoleRepository import RoleRepository

class UsersData:
  """ Create user data """
  def create_users():
    print ("Inserting users data")

    Users = [
      {
        'username' : "root",
        'password' : "b'gAAAAABhAjt7MwEbYu3qVcZN-_DcFut1TiDkzxQRuI-6roaqhK2pPceublesyqURIWRrXWJ04If2nKuJCTKq2zTGhRUCuUBjyQ=='",
        'email' : "nayookyaw@yahoo.com",
        'role_id' : "1"
      },
      {
        'username' : "developer",
        'password' : "b'gAAAAABhQFj8kTRfIcaAu9LVkQRzCJ1kSPnORiRFZqQH8mAYw-zyGjrFlPBSEsGfIP81D-T5gibYLxlGJqaXcZQq9FQqryb7Eg=='",
        'email' : "nayookyaw@yahoo.com",
        'role_id' : "1"
      },
      {
        'username' : "admin",
        'password' : "b'gAAAAABhAjt7m4DS9ICUhsMnX00f1nWYqMFqXwsZqRwY__-9E42TXp05v96alOWHLh1-gMkmY8kMDXuxvlQzEKvWiunBb7Uhyw=='",
        'email' : "admin@gmail.com",
        'role_id' : "2"
      },
      {
        'username' : "user",
        'password' : "b'gAAAAABhJ5BTv3sgwm8DpS-7gsZFl9yRVycomhthQCsEqPPX0F6GbXVYoK9Vclzgi6oVIyEc2CVHtCtcHX77GlXbqlkZtzkOhQ=='",
        'email' : "user@gmail.com",
        'role_id' : "3"
      }
    ]
    
    for user in Users:
      new_user = User(
        username = user['username'],
        password = user['password'],
        email = user['email'],
        role_id = user['role_id']
      )

      try:
        user = UserRepository.getUserByNameAndRoleID(user['username'], user['role_id'])
        if user == None :
          db.session.add(new_user)
          db.session.commit()

      except Exception as e:
        print (e)
        return jsonify({ "error" : 'Master Data can be run once time', "message" : str(e) })

    UsersData.create_roles()

    return jsonify({ "result" : "Succeed Users Adding!" })

  """ 
    Create role data 
    called inside UsersData create_users method
  """
  def create_roles():
    print ("Inserting roles data")

    Roles = [
      {
        'role_id' : 1,
        'role_name' : 'Root',
        'user_creation' : 1,
        'user_list' : 1,
        'role_creation' : 1,
      },
      {
        'role_id' : 2,
        'role_name' : 'Admin',
        'user_creation' : 1,
        'user_list' : 1,
        'role_creation' : 1,
      },
      {
        'role_id' : 3,
        'role_name' : 'User',
        'user_creation' : 0,
        'user_list' : 0,
        'role_creation' : 0,
      },
    ]
    
    for role in Roles:
      new_role = Role(
        role_name = role['role_name'],
        user_creation = role['user_creation'],
        user_list = role['user_list'],
        role_creation = role['role_creation'],
      )

      try:
        role = RoleRepository.getRoleByNameAndId(role['role_id'], role['role_name'])
        if role == None :
          RoleRepository.save(new_role)
      except Exception as e:
        print (e)
        return jsonify({ "error" : 'Master Data can be run once time', "message" : str(e) })

    return jsonify({ "result" : "Succeed Roles Adding!" })
    
    

