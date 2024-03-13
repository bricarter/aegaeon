from flask import current_app as app, request, redirect, url_for, flash, render_template

from . import db
from .models import User


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']

        try:
            existing_email = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()

            flash(message='that email is already in use, please login.', category='error')
            return redirect(url_for('login'))
        except:
            pass
        
        if request.form['password'] != request.form['confirm_password']:
            flash(message='passwords do not match', category='error')
            return render_template('register.html')
            
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home', name=first_name))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']

        try:
            user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()

        except:
            flash(message='email or password error', category='error')
            return render_template('login.html')

        if user.password != request.form['password']:
            flash(message='email or password error', category='error')
            return render_template('login.html')
        
        return redirect(url_for('home', name=user.first_name))

    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route('/home/<string:name>', methods=['GET'])
def home(name:str):
    return render_template('home.html', name=name)