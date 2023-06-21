from flask import Flask,render_template, request,redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///baza.db"
db = SQLAlchemy(app)
app.app_context().push()

    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(100), nullable=False)
with app.app_context():
    db.create_all()
Client.query.all()
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/cart")
def cart():
    return render_template("cart.html")
@app.route("/pizza")
def pizza():
    return render_template("pizza.html")
@app.route("/burger")
def burger():
    return render_template("burger.html")
@app.route("/tradycyjna")
def tradycyjna():
    return render_template("tradycyjna.html")
@app.route("/map")
def map():
    return render_template("map.html")

def map():
    return render_template("register.html")

@app.route('/login', methods =['GET', 'POST'])
def login():
    email_input = request.form.get('email')
    password_input = request.form.get('password')
    login_instance =Login()
    login_instance.log_in(email_input, password_input)
    login_instance.show_status()
    if session['login_session']:
        return redirect('/')
    print()
    return redirect('/login')

@app.route('/register', methods =['GET', 'POST'])
def register():
   email = request.form.get('email')
   password = request.form.get('password')
   password_2 = request.form.get('Repeat Rassword')
   firstname = request.form.get('Firstname')
   lastname = request.form.get('Lastname')
   number = request.form.get('number')
   print(Client.query.all())
   if len(password) <4:
       flash("Password is too short",'error')
       return redirect('/register')
   
   if password != password_2:
       flash("Password must be the same",'error')
       return redirect('/register')
   
   if Client.query.fitler_by(email=email).first():
       flash('This email is occupied','error')
       return redirect('/register')
   
   new_client = Client(email=email, password=password, firstname=firstname, lastname=lastname, number=number)
   db.session.add(new_client)
   db.session.commit()
   flash('register successfully')
   return redirect('login')

if __name__ =='__main__':
    app.run(debug=True,port=5001)