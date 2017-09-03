from flask import url_for, redirect, render_template, flash, g, session
from flask.ext.login import login_required
from app import app, lm

@app.route('/')
def index():
    return render_template('index.html')

