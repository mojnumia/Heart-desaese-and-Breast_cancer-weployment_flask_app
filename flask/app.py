from flask import Flask 
import numpy as np
from second import second
from templates.auth import auth
app=Flask(__name__)

app.register_blueprint(second)
app.register_blueprint(auth)

@app.route('/')
def test():
	return "hellow"

if __name__ == "__main__":
	app.run(debug=True)