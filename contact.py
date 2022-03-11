from flask import Flask
app = Flask(__name__)
@app.route("/contact")
def contact():
 return "<p>contact</p>"
if __name__  =='__main__':
    app.run()
    duebug = True