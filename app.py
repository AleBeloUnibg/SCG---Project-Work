from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
import mysql.connector
from mysql.connector import Error
from model_utils.articolo import Articolo
import os

# Initialize the Flask application
app = Flask(__name__)

# Get the root of the application (in this way we can run the app from outside the my_Flask_app folder)
root = app.root_path

# This configuration is necessary to use Flask sessions (they are signed with this secret)
app.secret_key = "Very Strong Password"

try:
    connection = mysql.connector.connect(host='localhost',
                                            database='sistemi_controllo_gestione',
                                            user='root',
                                            password='')
except Error as e:
    print("Error while connecting to MySQL", e)

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/')
def dashboard():
    costo_tot_budget = get_tot_budget(connection)

    # Simply render the template in templates/login/login.html
    return render_template("index.html", costo_budget = costo_tot_budget)   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/Centro_ricavo')
def analisiCentroRicavo():
    # Simply render the template in templates/login/login.html
    return render_template("Centro_ricavo.html")   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/budget_produzione')
def analisiBudget_produzione():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/budget_produzione.html")   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/consuntivo_produzione')
def analisiConsuntivo_produzione():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/consuntivo_produzione.html")   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/mixEffettivo_produzione')
def analisiMixEffettivo_Produzione():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/mixEffettivo_produzione.html")   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/mixStandard_produzione')
def analisiMixStandard_produzione():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/mixStandard_produzione.html")   # link al nome del template generato (si assume di essere già nella cartella template



# The app is served only if this file is run
if __name__ == '__main__':
    # Start the app on "localhost:5000"
    from main import get_tot_budget
    # The debug variable is used to automatically restart the server when code changes
    app.run(debug=True)
