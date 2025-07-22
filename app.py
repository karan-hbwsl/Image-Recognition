from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
from werkzeug.utils import secure_filename
from vision_match import find_top_matches

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

HTML_FORM = None  # No longer needed, using template file

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    matches = None
    uploaded_filename = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            uploaded_filename = filename
            # Run the matching algorithm
            matches = find_top_matches(upload_path, top_n=10)
    return render_template('index.html', matches=matches, uploaded_filename=uploaded_filename)

@app.route('/images/<filename>')
def static_image(filename):
    return send_from_directory('images', filename)

@app.route('/uploads/<filename>')
def uploaded_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True) 