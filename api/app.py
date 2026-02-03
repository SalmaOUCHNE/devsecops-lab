from flask import Flask, request, escape
import os
import hashlib

app = Flask(__name__)

# Clé secrète depuis variable d’environnement
SECRET_KEY = os.environ.get("SECRET_KEY", "change_me")

# Hash sécurisé (SHA-256)
def encrypt(data):
    return hashlib.sha256(data.encode()).hexdigest()

@app.route("/create-ticket")
def create_ticket():
    title = request.args.get("title", "")
    description = request.args.get("description", "")

    # Protection contre le XSS
    return f"<h2>{escape(title)}</h2><p>{escape(description)}</p>"

@app.route("/execute")
def execute():
    # Fonction désactivée pour éviter l’injection de commandes
    return "Forbidden", 403

@app.route("/auth")
def auth():
    password = request.args.get("password", "")
    ADMIN_HASH = encrypt("admin123")

    if encrypt(password) == ADMIN_HASH:
        return "Access granted"

    return "Access denied", 401

if __name__ == "__main__":
    app.run(debug=False)