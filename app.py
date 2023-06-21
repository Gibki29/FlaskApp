from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/cart")
@app.route("/login")
@app.route("/map")

def home():
    return render_template("index.html")
def cart():
    return render_template("cart.html")
def login():
    return render_template("login.html")
def map():
    return render_template("map.html")


if __name__ =='__main__':
    app.run(debug=True,port=5001)