from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField

class AddPetForm(FlaskForm):

    name = StringField("Name")
    species = StringField("What Kind of Pet?")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField("Comments")
    avail = BooleanField("Ready to Adopt?")

class EditPetForm(FlaskForm):

    photo_url = StringField("Update Photo")
    notes = TextAreaField("New Comments")
    avail = BooleanField("Still Available?")