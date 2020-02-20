from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField


class UploadForm(FlaskForm):
    image=FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])