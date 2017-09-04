from flask import render_template
from flask import request
from app import app
import solve

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def r_solve():
    print( request.form['letters'] )
    return solve.json_list(request.form['letters'])

