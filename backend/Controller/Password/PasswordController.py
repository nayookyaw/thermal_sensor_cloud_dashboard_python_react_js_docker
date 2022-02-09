from flask import render_template, request, jsonify, session, redirect
from __main__ import app, db
import secrets

from Models.User import User

from DAO.User.UserRepository import UserRepository

from constants import Constants

from Services.EncryptDecrypt import EncryptDecrypt

class PasswordController:

    def send_forgot_password_token():
        try:

            data = request.get_json('data')
            data_email = data['email']
            user = UserRepository.getUserByEmailAndIsAzure(data_email)

            if user == None :
                return jsonify({ "success": "", "message" : "No Email Match Found!", "data" : {} }), 200

            if user :
                randon_token = secrets.token_urlsafe()

                user.forgot_password_token = randon_token
                UserRepository.update(user)

                if (user.email) :

                    emailto = [user.email]
                    emailSubject = "Password Reset Link"
                    emailBody = "<h2>Hello " + user.username + ",</h2>"
                    emailBody += "<p>This is reset password link and please click to reset password</p>"
                    emailBody += "<a href='" + Constants.RESET_PASSWORD_HOST +"/reset_password?token=" + randon_token + "' target='_blank' style='text-decoration:none; margin-top:15px;'>Reset Password</a>" 
                    emailBody += "<br><br> <a href='" + Constants.RESET_PASSWORD_HOST +"/reset_password?token=" + randon_token + "' target='_blank' style='text-decoration:none;'><div style='background:#348EDA; color:white; width:75px; height:40px; line-height:40px; text-align:center'>Click</div></a>" 
                    emailBody += "<p>Thanks</p>"

                    # EmailUtil.send_email_smtp(emailto, emailSubject, emailBody)
                    
                    return jsonify({ "success":"", "message" : "Success! Please check Your Email. If you don't receive, <a href='#' onclick='forgot_password()'>Send Email</a> again", "data" : user.to_json() }), 200
                    
        except Exception as e:
            print (e)
            return jsonify({ "error" : "something is wrong" }), 400

    def reset_password():

        token = request.args.get("token")
        data = {
            'page' : 'reset_password',
            'token' : token
        }

        user = UserRepository.getUserByForgotPasswordToken(data['token'])

        if user == None :
            data['auth'] = False

        if user :
            data['auth'] = True

        return render_template("views/password/reset_password.html", data=data)

    def reset_password_and_change():
        try:

            data = request.get_json('data')
            data_token = data['token']
            user = UserRepository.getUserByForgotPasswordToken(data_token)

            if user == None :
                return jsonify({ "success": "", "message" : "Unauthorized! Reset Password Fail!", "data" : {} }), 200

            if user :
                data_new_password = data['new_password']
                data_new_password_encrypt = EncryptDecrypt.encrypt(data_new_password)
                user.password = data_new_password_encrypt
                user.forgot_password_token = None
                user.token = None
                UserRepository.update(user)

                return jsonify({ "success": "", "message" : "Reset Password Success!", "data" : user.to_json() }), 200
                
        except Exception as e:
            print (e)
            return jsonify({ "error" : "something is wrong" }), 400
