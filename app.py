from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html")


@app.route("/result")
def reuslt():
    output = request.form.to_dict()
    name = output[""]
    
    return render_template("index.html")
if __name__ =='__main__':
    app.run(debug=True,port=5001)