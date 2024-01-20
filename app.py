from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
load_dotenv()

# Config of api keys and database

# first two are in env file
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ALPHA_API_KEY = os.environ.get('ALPHA_API_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    stocks = db.relationship("Stock", backref='owner', lazy=True)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    market_cap = db.Column(db.Float, nullable=False)
    last_close_price = db.Column(db.Float, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User authentication routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password')
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("signup.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Dashboard and stock handling
@app.route('/dashboard')
@login_required
def dashboard():
    user_stocks = current_user.stocks
    return render_template("dashboard.html", stocks=user_stocks)

@app.route('/add_stock', methods=['POST'])
@login_required
def add_stock():
    if request.method == 'POST':
        stock_symbol = request.form['symbol']
        new_stock = Stock(symbol=stock_symbol, owner=current_user)
        db.session.add(new_stock)
        db.session.commit()
        flash('Stock added to your list!')
    return redirect(url_for('dashboard'))


def fetch_stock_data(symbol):

    pass



if __name__ == '__main__':
    app.run(debug=True)
