from flask import Flask, render_template, request

# flask app
app = Flask(__name__)


@app.route("/hello")
def index():
    return "Hello World!!"

# route for google-login
@app.route('/google-login')
def google_login():
    # google client id
    client_id = "548006263303-7f4qddq8glb3elfsajvdune2g8hfknh2.apps.googleusercontent.com"
    return render_template("login.html", client_id=client_id)



app.run(debug=True)
