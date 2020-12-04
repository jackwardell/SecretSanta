from flask_wtf import FlaskForm
from wtforms.fields import FieldList
from wtforms.fields import SubmitField
from wtforms.fields.html5 import EmailField
# from wtforms.validators import Email


class SecretSantaForm(FlaskForm):
    email_addresses = FieldList(EmailField("Email Address"))
    submit = SubmitField("Submit")
