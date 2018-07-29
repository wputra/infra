"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os
import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

app.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.db = SQLAlchemy(app.app)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser URL
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")

@app.route('/db')
def dbtest():
    try:
        app.db.create_all()
        return 'Database Connected \n'
    except Exception as e:
        return e.message + '\n'

if __name__ == '__main__':
    app.run(debug=True)