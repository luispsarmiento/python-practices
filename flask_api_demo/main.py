from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/me")
def me_api():
    return {
        "username": "Luis P. Sarmiento",
        "theme": "dark",
        ##"image": url_for("user_image", filename=user.image),
    }