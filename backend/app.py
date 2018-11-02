import os

from flask import Flask, request, render_template

TEMPLATE_FOLDER = os.path.abspath('./dist/')
STATIC_FOLDER = os.path.abspath('./dist/_nuxt/')
UPLOAD_FOLDER = '/tmp/simple_filer_upload/'

app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("file")
    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(file_path)

    return 'Upload success'


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', use_reloader=True, use_debugger=True)
