from flask import Blueprint, request, redirect, url_for, send_from_directory, current_app
from werkzeug.utils import secure_filename
import os

media_bp = Blueprint('media', __name__)

@media_bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('media.uploaded_file', filename=filename))

@media_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)




def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']