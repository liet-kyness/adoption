from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("What Kind of Pet?", choices=[("dog","Dog"), ("cat", "Cat"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Length(min=10), Optional()])
    avail = BooleanField("Ready to Adopt?", default=True)

class EditPetForm(FlaskForm):

    photo_url = StringField("Update Photo")
    notes = TextAreaField("New Comments")
    avail = BooleanField("Still Available?")