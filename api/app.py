from flask import Flask, request
import os
import hashlib

app = Flask(__name__)

#  Clé secrète codée en dur (mauvaise pratique)
SECRET_KEY = "secret123"

#  Fonction de chiffrement faible (SHA1)
def encrypt(data):
    return hashlib.sha1(data.encode()).hexdigest()

@app.route("/create-ticket")
def create_ticket():
    title = request.args.get("title")
    description = request.args.get("description")

    #  Vulnérabilité XSS (pas d’échappement)
    return f"<h2>{title}</h2><p>{description}</p>"

@app.route("/execute")
def execute():
    cmd = request.args.get("cmd")

    #  Injection de commande
    os.system(cmd)
    return "Command executed"

@app.route("/auth")
def auth():
    password = request.args.get("password")

    #  Authentification faible
    if encrypt(password) == encrypt("admin"):
        return "Access granted"

    return "Access denied"

if __name__ == "__main__":
    #  Mode debug activé
    app.run(debug=True)