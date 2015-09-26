import json

from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route('/')
# check if signed in:

def index():
	return render_template("home.html")

@app.route('/User')

@app.route('/User/Project')

@app.route('/register')



app.run(debug=True, port=8080)
