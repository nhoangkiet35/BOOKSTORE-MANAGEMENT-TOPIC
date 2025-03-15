from flask_wtf import FlaskForm
from wtforms import HiddenField, IntegerField


class AddToCart(FlaskForm):
    quantity = IntegerField("Quantity")
    id = IntegerField("ID")
