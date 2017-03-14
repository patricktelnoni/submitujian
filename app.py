from flask import (
                    Flask, render_template,
                    request, url_for, redirect,
                    flash, session, jsonify, send_from_directory)
from werkzeug.utils import secure_filename

import math, os

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['zip', 'rar'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/15-04'
app.config['SESSION_TYPE']  = 'filesystem'
app.config['SECRET_KEY']    = '12345678'
# sess = session()
# sess.init_app(app)

@app.route('/any')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def hitung():
    bil1    = request.form['angka1']
    bil2    = request.form['angka2']
    operasi = request.form['operasi']
    hasil = {
      'tambah'  : float(int(bil1)+int(bil2)),
      'kurang'  : float(int(bil1)-int(bil2)),
      'kali'    : float(int(bil1)*int(bil2))
    }.get(operasi, float(int(bil1)/int(bil2)))
    return render_template('hasil.html', bil1=bil1, bil2=bil2, hasil=hasil, operasi=operasi)

@app.route('/')
def upload_form():
    return render_template('upload-form.html')

@app.route('/file-upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('no file part')
            return redirect(request.url)
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'success'
            # return redirect(url_for('upload_file', filename=filename))
    else:
        filename =request.args.get('filename')
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/file-upload?filename=nama')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete-file', methods=['POST'])
def delete_file():
    file = request.form['deleted']
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))
    return 'success'


if __name__ == '__main__':
    app.run(
            host="0.0.0.0",
            port=int("5000"),
            debug=True
        )
