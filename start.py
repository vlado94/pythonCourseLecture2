#name = input()
#print("test  " + name)
#print(f"test {name}")
#print("{}".format(name))


class Point: 
	def __init__(self,x,y) :
		self.x = x
		self.y = y
		
p = Point(3,4)
print(p.x)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() :
	return "hello"
	
@app.route("/<string:name>")
def hi(name) :
	return f"hello {name}"
	
	