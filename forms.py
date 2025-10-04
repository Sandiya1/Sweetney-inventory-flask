from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional

class ProductForm(FlaskForm):
    product_id = IntegerField("Product ID", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Save")

class LocationForm(FlaskForm):
    name = StringField("Location Name", validators=[DataRequired()])
    submit = SubmitField("Save")

class MovementForm(FlaskForm):
    product = SelectField('Product', coerce=int, validators=[DataRequired()])
    from_location = SelectField('From Location', choices=[], validators=[Optional()])
    to_location = SelectField('To Location', choices=[], validators=[Optional()])
    qty = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Record Movement')