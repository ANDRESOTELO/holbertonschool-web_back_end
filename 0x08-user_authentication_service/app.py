#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """
    Method: GET
    Return: Welcome message
    """
    return jsonify({"message": "Bienvenue"})
