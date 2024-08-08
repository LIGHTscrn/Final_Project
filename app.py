from flask import Flask, redirect,render_template, request,session
from flask_session import Session
from werkzeug.security import apology,login_required,lookup

#config

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

