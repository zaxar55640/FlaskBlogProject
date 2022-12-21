from flask import Blueprint, render_template, redirect, url_for, request
from entities.place import Places
from entities.user import User
from flask_login import login_required, login_user, logout_user, current_user
from Forms.RegisterForm import RegisterForm
from Forms.LoginForm import LoginForm
from Forms.PlaceForm import PlaceForm
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template("main/map.html")


@main.route('/places')
def viewPlaces():
    info = f'Places:'
    places = Places.query.order_by(Places.date.desc()).all()
    return render_template("main/places.html", places=places, info=info)

@main.route('/create/place', methods=['GET', 'POST'])
def createPlace():
    form = PlaceForm()
    if form.validate_on_submit():
        place = Places(title=form.title.data, text=form.text.data, area=form.area.data, img=form.img.data)
        try:
            db.session.add(place)
            db.session.commit()
        except:
            return "Error"

        return '<h1>New place has been created!</h1>'
    else:
        return render_template("main/createPlace.html", form=form)


@main.route('/signup', methods=['GET', 'POST'])
def signUp():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.name.data, email=form.email.data, psw=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'

    return render_template('main/signup.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.psw, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('.home'))

        return '<h1>Invalid username or password</h1>'

    return render_template('main/login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.home'))

@main.route('/userpage')
@login_required
def userpage():
    user = current_user._get_current_object()
    return render_template('main/userpage.html')

@main.route('/visited')
@login_required
def visited():
    user = current_user._get_current_object()
    places = user.visited
    info = f"{user.username}'s visited places:"
    return render_template("main/places.html", places=places, info=info)