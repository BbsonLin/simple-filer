import os

from flask import Flask, jsonify, current_app, render_template, url_for
from flask_filer import Filer
from flask_cors import CORS

TEMPLATE_FOLDER = os.path.abspath('../frontend/dist/')
STATIC_FOLDER = os.path.abspath('../frontend/dist/_nuxt/')
UPLOAD_FOLDER = '/tmp/'

app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
app.config['FILER_ROOT_PATH'] = UPLOAD_FOLDER
filer = Filer(app)
cors = CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map', methods=['GET'])
def map():
    def has_no_empty_params(rule):
        defaults = rule.defaults if rule.defaults is not None else ()
        arguments = rule.arguments if rule.arguments is not None else ()
        return len(defaults) >= len(arguments)

    links = []
    for rule in current_app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return jsonify(data=links)
