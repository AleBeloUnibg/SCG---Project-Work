from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
import mysql.connector
from mysql.connector import Error
from model_utils.articolo import Articolo
from main import get_costo_produzione_tot_budget
from main import get_costo_MP_tot_budget
from main import get_prezzo_tot_budget
from main import get_costo_produzione_tot_consuntivo
from main import get_costo_MP_tot_consuntivo
from main import get_prezzo_tot_consuntivo
from main import get_costo_produzione_tot_std
from main import get_costo_MP_tot_std
from main import get_prezzo_tot_std
from main import get_costo_produzione_tot_eff
from main import get_costo_MP_tot_eff
from main import get_prezzo_tot_eff

from main import get_costo_produzione_x_art_budget
from main import get_costo_MP_x_art_budget
from main import get_costo_produzione_x_art_consuntivo
from main import get_costo_MP_x_art_consuntivo
from main import get_prezzo_x_art_budget
from main import get_prezzo_x_art_consuntivo
from main import get_quantita_prodotte_x_art_budget
from main import get_quantita_prodotte_x_art_consuntivo
from main import get_quantita_vendute_x_art_budget
from main import get_quantita_vendute_x_art_consuntivo
from main import get_mix_std
from main import set_quantita_prodotte_x_art_std
from main import set_quantita_vendute_x_art_std
from main import get_mix_eff
from main import set_quantita_prodotte_x_art_eff
from main import set_quantita_vendute_x_art_eff
from main import set_scostamento_volume
from main import set_scostamento_mix
from main import set_scostamento_prezzo_costo

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

list_articoli = []

get_costo_produzione_x_art_budget(connection, list_articoli)
get_costo_MP_x_art_budget(connection, list_articoli)
get_prezzo_x_art_budget(connection, list_articoli)
get_quantita_prodotte_x_art_budget(connection, list_articoli)
get_quantita_vendute_x_art_budget(connection, list_articoli)

get_costo_produzione_x_art_consuntivo(connection, list_articoli)
get_costo_MP_x_art_consuntivo(connection, list_articoli)
get_prezzo_x_art_consuntivo(connection, list_articoli)
get_quantita_prodotte_x_art_consuntivo(connection, list_articoli)
get_quantita_vendute_x_art_consuntivo(connection, list_articoli)

get_mix_std(connection, list_articoli)
set_quantita_prodotte_x_art_std(list_articoli)
set_quantita_vendute_x_art_std(connection,list_articoli)

get_mix_eff(connection, list_articoli)
set_quantita_prodotte_x_art_eff(list_articoli)
set_quantita_vendute_x_art_eff(connection, list_articoli)

set_scostamento_volume(list_articoli)
set_scostamento_mix(list_articoli)
set_scostamento_prezzo_costo(list_articoli)

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/')
def dashboard():
    costo_produzione_tot_budget = get_costo_produzione_tot_budget(list_articoli)
    costo_MP_tot_budget = get_costo_MP_tot_budget(list_articoli)
    prezzo_tot_budget = get_prezzo_tot_budget(connection)

    costo_produzione_tot_consuntivo = get_costo_produzione_tot_consuntivo(list_articoli)
    costo_MP_tot_consuntivo = get_costo_MP_tot_consuntivo(list_articoli)
    prezzo_tot_consuntivo = get_prezzo_tot_consuntivo(connection)

    delta_volume = sorted(list_articoli, key=lambda x: x.getQuantitaVenduta("STANDARD")-x.getQuantitaVenduta("BUDGET"), reverse=True)
    delta_mix = sorted(list_articoli, key=lambda x: x.getMix("EFFETTIVO")-x.getMix("STANDARD"), reverse=True)
    delta_prezzo_costo = sorted(list_articoli, key=lambda x: x.getQuantitaVenduta("CONSUNTIVO"), reverse=True)

    # Simply render the template in templates/login/login.html
    return render_template("index.html",
    mol_budget = prezzo_tot_budget - costo_produzione_tot_budget - costo_MP_tot_budget,
    mol_consuntivo = prezzo_tot_consuntivo - costo_produzione_tot_consuntivo - costo_MP_tot_consuntivo,
    scostamento_volume = delta_volume,
    scostamento_mix = delta_mix,
    scostamento_prezzo = delta_prezzo_costo)   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/Centro_ricavo')
def analisiCentroRicavo():
    costo_produzione_tot_budget = get_costo_produzione_tot_budget(list_articoli)
    costo_MP_tot_budget = get_costo_MP_tot_budget(list_articoli)
    prezzo_tot_budget = get_prezzo_tot_budget(connection)

    prezzo_tot_std = get_prezzo_tot_std(connection)
    costo_produzione_tot_std = get_costo_produzione_tot_std(list_articoli)
    costo_MP_tot_std = get_costo_MP_tot_std(list_articoli)

    prezzo_tot_eff = get_prezzo_tot_eff(connection)
    costo_produzione_tot_eff = get_costo_produzione_tot_eff(list_articoli)
    costo_MP_tot_eff = get_costo_MP_tot_eff(list_articoli)

    costo_produzione_tot_consuntivo = get_costo_produzione_tot_consuntivo(list_articoli)
    costo_MP_tot_consuntivo = get_costo_MP_tot_consuntivo(list_articoli)
    prezzo_tot_consuntivo = get_prezzo_tot_consuntivo(connection)

    # Simply render the template in templates/login/login.html
    return render_template("Centro_ricavo.html",
    p_budget = prezzo_tot_budget,
    c_produzione_budget = costo_produzione_tot_budget,
    c_MP_budget = costo_MP_tot_budget,

    p_std = prezzo_tot_std,
    c_produzione_std = costo_produzione_tot_std,
    c_MP_std = costo_MP_tot_std,

    p_eff = prezzo_tot_eff,
    c_produzione_eff = costo_produzione_tot_eff,
    c_MP_eff = costo_MP_tot_eff,

    p_consuntivo = prezzo_tot_consuntivo,
    c_produzione_consuntivo = costo_produzione_tot_consuntivo,
    c_MP_consuntivo = costo_MP_tot_consuntivo)   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/budget_produzione')
def analisiBudget_produzione():
    return render_template("C_ricavo/budget_produzione.html", list = list_articoli)   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/consuntivo_produzione')
def analisiConsuntivo_produzione():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/consuntivo_produzione.html", list = list_articoli)   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/mixEffettivo_produzione')
def analisiMixEffettivo_Produzione():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/mixEffettivo_produzione.html", list = list_articoli)   # link al nome del template generato (si assume di essere già nella cartella template

# @app.route specify the exposed URL, in this case it is "http://my_site.com/"
@app.route('/mixStandard_produzione')
def analisiMixStandard_produzione():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/mixStandard_produzione.html", list = list_articoli)   # link al nome del template generato (si assume di essere già nella cartella template

@app.route('/articolo', methods=['GET'])
def articolog():
    # Simply render the template in templates/login/login.html
    return render_template("C_ricavo/articolo.html")   # link al nome del template generato (si assume di essere già nella cartella template

@app.route('/articolo', methods=['POST'])
def articolop():
    articolo = request.form['articolo']

    for art in list_articoli:
        if art.getCodice() == articolo:
            return render_template("C_ricavo/articolo.html", art = art)
    return "Articolo non trovato"



# The app is served only if this file is run
if __name__ == '__main__':
    # Start the app on "localhost:5000"
    # The debug variable is used to automatically restart the server when code changes
    app.run(debug=True)
