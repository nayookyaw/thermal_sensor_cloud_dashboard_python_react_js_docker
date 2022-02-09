from flask import render_template, request, jsonify, session, redirect
from __main__ import app, db
import secrets

""" phyo import """
import flask_login
from Models.User import User
from flask.helpers import url_for
from functools import wraps
from DAO.User.UserRepository import UserRepository

from Services.EncryptDecrypt import EncryptDecrypt

class LoginController:

    def login_auth():
        try:

            session.clear() # for AuthController.require_authorization

            print("in.............................")
            session['logged_in'] = True
            # session.permanent = True
            # session.modified = True
            data = request.get_json('data')
            data_user = data['username']
            data_password = data['password'] 
    
            user = UserRepository.searchUserByName(data_user)

            if user == None :
                return jsonify({ "error" : "Invalid Username!", "data" : {} }), 200
            else :
                user_password = bytes(user.password[slice(2, len(user.password)-1)], 'utf-8')
                decrypt_password = EncryptDecrypt.decrypt(user_password)

                if data_password == decrypt_password :
                    flask_login.login_user(user, remember=False)

                    randon_token = secrets.token_urlsafe()

                    user.token = randon_token
                    db.session.commit()

                    session['auth_login'] = {
                        "username" : user.username,
                        "role_id" : user.role_id,
                        "token" : user.token
                    }

                    return jsonify({ "success" : "Authorize", "data" : user.to_json() }), 200
                else :
                    return jsonify({ "error" : "Invalid Password!", "data" : {} }), 200
                
        except Exception as e:
            print (e)
            return jsonify({ "error" : "something is wrong" }), 400

    def logout():
        try:
            
            return jsonify({ "success" : "Logout Success!" }), 200
        except Exception as e:
            print (e)
            return jsonify({ "error" : "Unauthorized" }), 400
