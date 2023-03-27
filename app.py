from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_proj'
app.config['SECRET_KEY'] = 'asdfg123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/pets/<int:pet_id>')
def show_pet(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('show.html', pet=pet)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        spec = form.species.data
        url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        avail = form.avail.data

        new_pet = Pet(
            name = name,
            species = spec,
            photo_url = url,
            age = age,
            notes = notes,
            avail = avail
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added!")
        return redirect('/')
    else:
        return render_template('add.html', form=form)
    
@app.route('/pets/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    
    pet = Pet.query.get(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.avail = form.avail.data
        
        db.session.commit()

        flash(f"{pet.name} updated!")
        return redirect('/')
    else:
        return render_template('show.html', pet=pet, form=form)

