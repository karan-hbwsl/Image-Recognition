from flask import Flask, request, render_template_string, send_from_directory, redirect, url_for
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

HTML_FORM = '''
<!doctype html>
<title>Image Recognition Upload</title>
<h1>Upload an image to find matches</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file required>
  <input type=submit value=Upload>
</form>
{% if matches %}
  <h2>Top 10 Matches:</h2>
  <div style="display: flex; flex-wrap: wrap;">
  {% for filename, score in matches %}
    <div style="margin: 10px; text-align: center;">
      <img src="{{ url_for('static_image', filename=filename) }}" width="150" style="display: block; margin-bottom: 5px;"/>
      <div>{{ filename }}<br/>Score: {{ score }}</div>
    </div>
  {% endfor %}
  </div>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    matches = None
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
            # Run the matching algorithm
            matches = find_top_matches(upload_path, top_n=10)
    return render_template_string(HTML_FORM, matches=matches)

@app.route('/images/<filename>')
def static_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True) 