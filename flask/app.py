from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('svelte_main.html', page="index", extra_data=json.dumps({'current_user': "insert user check function here", 'test': "This is a test",}))

@app.route("/login")
def login_page():
    return render_template('svelte_main.html', page="login", extra_data=json.dumps({'current_user': "no user yet!", 'test': "mor testing",}))

@app.route("/signup")
def signup_page():
    return render_template('svelte_main.html', page="signup", extra_data=json.dumps({'current_user': "Want to be a user?", 'test': "This is another test",}))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)