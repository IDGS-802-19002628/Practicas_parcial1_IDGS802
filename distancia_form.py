from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField

class UseForm(Form):
    x1 = StringField("x1")
    y1 = StringField("y1")
    x2 = StringField("x2")
    y2 = StringField("y2")
    