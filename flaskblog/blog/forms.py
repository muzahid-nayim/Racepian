from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
from flask_ckeditor import CKEditorField



# ========================================
# ==============Post Form=================
# ========================================

class PostForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    # content = TextAreaField('Content',validators=[DataRequired()])
    content = CKEditorField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')