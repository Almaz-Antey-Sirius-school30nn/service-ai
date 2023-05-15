import os

from flask import Flask

app_name = os.path.abspath(os.path.dirname(__file__)) + "\\" + __name__


app = Flask(app_name)
