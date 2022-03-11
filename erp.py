from flask import Flask 
from flask import render_template
app  = Flask(__name__)

@app.route('/')
def Home():
 return render_template("Home.html")

@app.route('/login')
def login():
   return render_template("login.html",title="Login")

@app.route('/logout')
def logout():
    return render_template("logout.html")

@app.route('/register')
def register():
    return render_template("register.html",title="Register")

@app.route('/profile')
def profile():
    return "My Profile"

@app.route("/contact")
def contact():
 return "contact"

if __name__ == '__main__':
    app.run()
    


    