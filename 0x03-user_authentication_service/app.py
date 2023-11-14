#!/usr/bin/env python3
""" flask app """

from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/')
def home():
    data = {"message": "Bienvenue"}
    return jsonify(data)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ handles credentials """
    email = request.form.get('email')
    passwd = request.form.get('password')
    try:
        user = AUTH.register_user(email, passwd)
        return jsonify({
            'email': email,
            'message': 'user created'
        })
    except Exception:
        pass
    return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
