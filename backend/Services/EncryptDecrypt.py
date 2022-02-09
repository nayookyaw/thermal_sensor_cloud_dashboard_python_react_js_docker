from flask import render_template, request, jsonify
from __main__ import app

from constants import Constants

from cryptography.fernet import Fernet

class EncryptDecrypt:

    def encrypt(message):
        secret_key = Constants.ENCRYPT_DECRYPT_SECRET_KEY

        try :
            fernet = Fernet(secret_key)
            encrpt_msg = fernet.encrypt(message.encode())
            return encrpt_msg
        except Exception as e:
            print (e)
            return "error during encrypting string!"

    def decrypt(encrypt_msg):
        secret_key = Constants.ENCRYPT_DECRYPT_SECRET_KEY

        try :
            fernet = Fernet(secret_key)
            decrypt_msg = fernet.decrypt(encrypt_msg).decode()
            return decrypt_msg
        except Exception as e:
            print (e)
            return "error during decrypting string!"