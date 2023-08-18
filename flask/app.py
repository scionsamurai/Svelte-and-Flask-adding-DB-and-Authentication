from flask import Flask, redirect, request, flash
from flask_login import login_user, LoginManager, logout_user, login_required
from flask import render_template
import json

from utils import redirect_back, check_user
from sql_utils import User

app = Flask(__name__)

app.secret_key = "sassdfsdfs3sdfdfdadsf2423442sdfasdf2fb3443b4"
login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route("/")
@login_required
def home():
    return render_template('svelte_main.html', page="index", styles="global.css", extra_data=json.dumps({'current_user': check_user(), 'test': "This is a test",}))

@app.route("/signup")
def signup_page():
    return render_template('svelte_main.html', page="signup", styles="loginSignup.css", extra_data=json.dumps({'current_user': check_user(), 'test': "This is another test"}))

# https://atrium.ai/resources/how-to-implement-oauth-2-0-login-for-python-flask-web-server-applications/      <-----------add oauth
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        
        user = User(name, password, email)
        errors = user.is_valid(confirm_password)
        if errors[0]:
            user.save_to_db()
            
            login_user(user, remember=True)
            
            flash("Account created successfully", "success")
            return redirect_back('home')
        else:
            for error in errors[1]:
                flash(error, "error")
            return redirect_back('signup_page')
    else:
        return redirect_back('signup_page')

@app.route("/login")
def login_page():
    return render_template('svelte_main.html', page="login", styles="loginSignup.css", extra_data=json.dumps({'current_user': check_user(), 'test': "mor testing",}))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        user = User(name, password)
        if user.is_authenticated():
            login_user(user, remember=True)
            return redirect_back('home')
        else:
            return redirect_back('login_page')
    else:
        return redirect_back('login_page')

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect('/')

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect('/login')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
