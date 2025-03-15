from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField


class Checkout(FlaskForm):
    customer_id = HiddenField("Id")
    full_name = StringField("Full name")
    phone_number = StringField("Number")
    email = StringField("Email")
    address = StringField("Address")
    payment_type = SelectField("Payment Type")
