from flask import Flask, request
import os
import hashlib

app = Flask(__name__)

# Clé secrète hardcodée (fausse)
SECRET_KEY = "secret123"

# Hash faible (SHA1)
def encrypt(data):
    return hashlib.sha1(data.encode()).hexdigest()

@app.route("/create-ticket")
def create_ticket():
    title = request.args.get("title")
    description = request.args.get("description")

    # XSS (ما كاين حتى حماية)
    return f"<h2>{title}</h2><p>{description}</p>"

@app.route("/execute")
def execute():
    cmd = request.args.get("cmd")

    # Command Injection (CRITIQUE)
    os.system(cmd)
    return "Command executed"

@app.route("/auth")
def auth():
    password = request.args.get("password")

    # Auth faible + mot de passe ثابت
    if encrypt(password) == encrypt("admin"):
        return "Access granted"
    return "Access denied"

if __name__ == "__main__":
    # Debug مفعّل (خطر)
    app.run(debug=True)