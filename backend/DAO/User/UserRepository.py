from flask import request, session
import json

from Models.User import User
from Models.Role import Role
from sqlalchemy import func, desc

from __main__ import db
from operator import and_, or_

class UserRepository:

    def save(user):
        db.session.add(user)
        db.session.commit()
    
    def update():
        db.session.commit()

    def searchUserByName(username):
        print('get--------------------')
        filter_group = and_(User.deleted_at.is_(None), Role.deleted_at.is_(None))
        filter_group = and_(filter_group, User.username == func.binary(username))
        user = User.query.filter(filter_group).first()
        return user

    def getUser():
        user = User.query.filter_by(deleted_at = None).all()
        return user

    def getUserCount():
        filter_group = and_(User.deleted_at.is_(None), Role.deleted_at.is_(None))
        filter_group = and_(filter_group, User.username != 'developer')
        auth_login = session['auth_login']
        role_id = auth_login.get('role_id')
        if role_id == str(2) :
            filter_group = and_(filter_group, User.role_id != str(1))
        elif role_id != str(1) and role_id != str(2) :
            filter_group = and_(filter_group, User.role_id != str(1))
            filter_group = and_(filter_group, User.role_id != str(2))
        user_count = User.query.outerjoin(Role, Role.role_id == User.role_id).filter(
            filter_group).add_columns(Role.role_name).count()
        return user_count

    def getUsers(data):
        filter_group = and_(User.deleted_at.is_(None), Role.deleted_at.is_(None))
        filter_group = and_(filter_group, User.username != 'developer')
        auth_login = session['auth_login']
        role_id = auth_login.get('role_id')
        if role_id == str(2) :
            filter_group = and_(filter_group, User.role_id != str(1))
        elif role_id != str(1) and role_id != str(2) :
            filter_group = and_(filter_group, User.role_id != str(1))
            filter_group = and_(filter_group, User.role_id != str(2))
        offset = data['offset']
        limit = data['limit']
        offset_value = offset if (offset == 0 or offset > 0) else 0
        limit_value = limit if limit > 0 else None
        users = User.query.outerjoin(Role, Role.role_id == User.role_id).filter(
            filter_group).add_columns(Role.role_name).order_by(
                desc(User.id)).offset(offset_value).limit(limit_value).all()
        return users

    def getUserById(id):
        filter_group = and_(User.deleted_at.is_(None), User.id==id)
        user = User.query.filter(filter_group).first()
        return user

    def getUserByNameAndToken(username, token):
        user = User.query.filter(User.username == func.binary(username), User.token == token, User.deleted_at == None).first()
        return user

    def getUserByNameAndRoleID(username, role_id):
        user = User.query.filter(User.username == func.binary(username), User.role_id == role_id, User.deleted_at == None).first()
        return user

    def getUserByEmailAndIsAzure(email):
        user = User.query.filter(User.email == func.binary(email), User.is_azure == None, User.deleted_at == None).first()
        return user
    
    def getUserByForgotPasswordToken(token):
        user = User.query.filter(User.forgot_password_token == func.binary(token), User.deleted_at == None).first()
        return user

    def getUserByExceptIdAndName(id, username):
        user = User.query.filter(User.id != id, User.username == func.binary(username), User.deleted_at == None).first()
        return user  

    def getUserByRoleId(role_id):
        filter_group = and_(User.deleted_at.is_(None), User.role_id==role_id)
        user = User.query.filter(filter_group).first()
        return user
