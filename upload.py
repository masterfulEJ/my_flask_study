import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
# from flask.ext.uploads import UploadSet, configure_uploads, ALL

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.mkdir(app.config['UPLOAD_FOLDER'])
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html')

if __name__ == '__main__':
	app.run(debug=True)