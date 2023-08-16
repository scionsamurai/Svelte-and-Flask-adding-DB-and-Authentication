from flask import Flask, redirect, request
from flask_login import login_user, LoginManager, logout_user, login_required
from flask import render_template
import json

from utils import redirect_back
from sql_utils import User

app = Flask(__name__)

app.secret_key = "sassdfsdfs3sdfdfdadsf2423442sdfasdf2fb3443b4"
login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route("/")
@login_required
def home():
    return render_template('svelte_main.html', page="index", extra_data=json.dumps({'current_user': "insert user check function here", 'test': "This is a test",}))

@app.route("/login")
def login_page():
    return render_template('svelte_main.html', page="login", extra_data=json.dumps({'current_user': "no user yet!", 'test': "mor testing",}))

@app.route("/signup")
def signup_page():
    return render_template('svelte_main.html', page="signup", extra_data=json.dumps({'current_user': "Want to be a user?", 'test': "This is another test",}))


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
            return render_template('svelte_main.html', page='login')
    else:
        return render_template('svelte_main.html', page='login')

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
