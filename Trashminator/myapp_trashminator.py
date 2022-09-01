from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from trash_detector import detectorTrash
import os
app = Flask(__name__)

# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')

@app.route('/nofile', methods=['GET', 'POST'])
def nofile():
   return render_template('nofile.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file_upload']
      if f.filename == '':
         return nofile()
      f.save(secure_filename(f.filename))
      file_path = os.path.abspath(f.filename)
      return file_path

if __name__ == '__main__':
   app.run(debug = True, port=5000)


