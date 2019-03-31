from flask import Flask, render_template,session,request
from flask_session import Session

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)

#app.config("SESSION_PERMANENT") = False
#app.config("SESSION_TYPE") = "filesystem"
Session(app)
	
	
#@app.route("/<string:name>")
#def hi(name):
#	return "hello " + name

@app.route("/",methods=['GET', 'POST'])
def index() :
	if session.get("notes") is None:
		session["notes"] = []
	if request.method == "POST" :
		name = request.form.get("name")
		session.get("notes").append(name)
	return render_template("index.html",names = session.get("notes"))