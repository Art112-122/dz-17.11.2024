from flask import render_template
from app import app


@app.get('/')
def main():
    return render_template('main.html')
