# Import Form and RecaptchaField (optional)
from flask_wtf import Form  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, TextAreaField # BooleanField
from wtforms.fields import StringField, HiddenField
from wtforms.widgets import TextArea
# Import Form validators
from wtforms.validators import Required, Email, EqualTo, Length


# Define the login form (WTForms)

class NotesForm(Form):
    message = TextAreaField('Text', render_kw={"rows": 3})
    id = HiddenField('Text')   