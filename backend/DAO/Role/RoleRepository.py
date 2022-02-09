from flask import request
import json

from Models.Role import Role
from sqlalchemy import func, desc

from __main__ import db
from operator import and_, or_

class RoleRepository:
    
    def save(role):
        db.session.add(role)
        db.session.commit()
    
    def update():
        db.session.commit()

    def getRoleByNameAndId(role_id, role_name):
        role = Role.query.filter(Role.role_id == role_id, Role.role_name == func.binary(role_name), Role.deleted_at == None).first()
        return role

    def getRoleCount():
        filter_group = Role.deleted_at.is_(None)
        filter_group = and_(filter_group, Role.role_name != 'Root')
        filter_group = and_(filter_group, Role.role_name != 'Super')
        role_count = Role.query.filter(filter_group).count()
        return role_count

    def getRole(data):
        filter_group = Role.deleted_at.is_(None)
        filter_group = and_(filter_group, Role.role_name != 'Root')
        filter_group = and_(filter_group, Role.role_name != 'Super')
        offset = data['offset']
        limit = data['limit']
        offset_value = offset if (offset == 0 or offset > 0) else 0
        limit_value = limit if limit > 0 else None
        roles = Role.query.filter(filter_group).order_by(
                desc(Role.role_id)).offset(offset_value).limit(limit_value).all()
        return roles

    def getRoles():
        filter_group = Role.deleted_at.is_(None)
        filter_group = and_(filter_group, Role.role_name != 'Root')
        filter_group = and_(filter_group, Role.role_name != 'Super')
        roles = Role.query.filter(filter_group).all()
        return roles

    def getRoleById(role_id):
        role = Role.query.filter(Role.role_id == role_id, Role.deleted_at == None).first()
        return role  

    def getRoleByName(role_name):
        role = Role.query.filter(Role.role_name == func.binary(role_name), Role.deleted_at == None).first()
        return role  

    def getRoleByExceptIdAndName(role_id, role_name):
        role = Role.query.filter(Role.role_id != role_id, Role.role_name == func.binary(role_name), Role.deleted_at == None).first()
        return role  