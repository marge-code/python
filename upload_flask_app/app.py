#!/usr/bin/env python

from flask import Flask, request, redirect, render_template

import logging

import cvsreader

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 * 1024

def init_logger():
    logger = logging.getLogger('upload-app')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template("upload_file.html")

    logger.info('handle POST request')
    productsReader = cvsreader.CvsProductsReader(request.stream)

    while True:
        new_product = productsReader.get_product()
        if not new_product:
            return "completed!"

logger = init_logger()
app.run(debug=False)

