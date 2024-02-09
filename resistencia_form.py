from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField

class UseForm(Form):
    r1 = SelectField(choices=[("0", "Negro",), ("1", "cafe"), ('2', 'rojo'),('3', 'naraja'), ('4', 'amarillo'), ('5', 'verde'), ('6', 'azul'), ('7', 'violeta'), ('8', 'gris'), ('9', 'blanco')])
    r2 = SelectField(choices=[("0", "Negro",), ("1", "cafe"), ('2', 'rojo'),('3', 'naraja'), ('4', 'amarillo'), ('5', 'verde'), ('6', 'azul'), ('7', 'violeta'), ('8', 'gris'), ('9', 'blanco')])
    r3 = SelectField(choices=[("", "Negro",), ("0", "cafe"), ('00', 'rojo'),('000', 'naraja'), ('0000', 'amarillo'), ('00000', 'verde'), ('000000', 'azul'), ('0000000', 'violeta'), ('00000000', 'gris'), ('000000000', 'blanco')])
    radios = RadioField('Tolerancia', choices=[('0.10', 'Plata'), ('0.05','Oro')])
    