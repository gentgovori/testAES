from flask import Flask, render_template, url_for, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import sqlalchemy
from datetime import datetime
from crypto import encrypt
from crypto import decrypt

app = Flask(__name__)





@app.route('/',methods=['POST','GET'])


def index():
    return render_template('index.html')



@app.route('/_enkriptoAES', methods=['GET', 'POST'])
def _enkriptoAES():
    if request.method == "POST":
        data =request.get_json()
        password = data["password"]
        plain_text = data["plain_text"]
        encrypted = encrypt(plain_text, password)
        return encrypted

@app.route('/_dekriptoAES', methods=['GET', 'POST'])
def _dekriptoAES():
    if request.method == "POST":
        data = request.get_json()
        password = data["password"]
        decrypted = decrypt(data,password)
        return decrypted

        


if __name__ == "__main__":
     app.run(debug=True)