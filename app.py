from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/cart")
def cart():
    return render_template("cart.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/map")
def map():
    return render_template("map.html")


if __name__ =='__main__':
    app.run(debug=True,port=5001)