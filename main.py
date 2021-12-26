import mysql.connector
from mysql.connector import Error
from model_utils.articolo import Articolo
from decimal import Decimal

def query(connection, sql_select_Query):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
    return records

def amongUs(list_articoli, codArt):
    for art in list_articoli:
        if art.codArt == codArt:
            return art
    art = Articolo(codArt)
    list_articoli.append(art)
    return art

def get_costo_x_art_budget(connection, list_articoli):
        
    sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, (costo_produzione_budget_x_art.C_unit + costo_mp_budget_x_art.costo_unita) as costo_unitario from costo_produzione_budget_x_art, costo_mp_budget_x_art where costo_produzione_budget_x_art.codArt = costo_mp_budget_x_art.codArt "
    records = query(connection, sql_select_Query)
    
    for row in records:
        costo_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setCosto(costo_tot_articolo_budget, "BUDGET")

def get_costo_x_art_consuntivo(connection, list_articoli):

    sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, (costo_produzione_consuntivo_x_art.C_unit + costo_mp_consuntivo_x_art.costo_unita) as costo_unitario from costo_produzione_consuntivo_x_art, costo_mp_consuntivo_x_art where costo_produzione_consuntivo_x_art.codArt = costo_mp_consuntivo_x_art.codArt "
    records = query(connection, sql_select_Query)
    
    for row in records:
        costo_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setCosto(costo_tot_articolo_consuntivo, "CONSUNTIVO")

def get_prezzo_x_art_budget(connection, list_articoli):

    sql_select_Query = "SELECT vendite_budget_x_art.codArt, vendite_budget_x_art.P_unit as P_unit from vendite_budget_x_art"
    records = query(connection, sql_select_Query)
    
    for row in records:
        prezzo_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setPrezzo(prezzo_tot_articolo_budget, "BUDGET")

def get_prezzo_x_art_consuntivo(connection, list_articoli):

    sql_select_Query = "SELECT vendite_consuntivo_x_art.CodArt, vendite_consuntivo_x_art.P_unit as P_unit from vendite_consuntivo_x_art "
    records = query(connection, sql_select_Query)

    for row in records:
        prezzo_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setPrezzo(prezzo_tot_articolo_consuntivo, "CONSUNTIVO")

def get_quantita_vendute_x_art_budget(connection, list_articoli):
    
    sql_select_Query = "SELECT vendite_budget_x_art.codArt, vendite_budget_x_art.qta as P_unit from vendite_budget_x_art "
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaVenduta(quantita_tot_articolo_budget, "BUDGET")


def get_quantita_vendute_x_art_consuntivo(connection, list_articoli):
    
    sql_select_Query = "SELECT vendite_consuntivo_x_art.codArt, vendite_consuntivo_x_art.qta as P_unit from vendite_consuntivo_x_art "
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaVenduta(quantita_tot_articolo_consuntivo, "CONSUNTIVO")

def get_quantita_prodotte_x_art_budget(connection, list_articoli):
    
    sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, costo_produzione_budget_x_art.qta as P_unit from costo_produzione_budget_x_art "
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaProdotta(quantita_tot_articolo_budget, "BUDGET")


def get_quantita_prodotte_x_art_consuntivo(connection, list_articoli):
    
    sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, costo_produzione_consuntivo_x_art.qta as P_unit from costo_produzione_consuntivo_x_art "
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaProdotta(quantita_tot_articolo_consuntivo, "CONSUNTIVO")

def get_costo_tot_budget(list_articoli):
    costo_budget = 0
              
    for x in list_articoli:
        if(x.getQuantitaProdotta("BUDGET") != 0):
            costo_budget += x.getQuantitaProdotta("BUDGET") 
    
    return costo_budget

def get_prezzo_tot_budget(list_articoli):
    prezzo_budget = 0
              
    for x in list_articoli:
        prezzo_budget += Decimal(x.getPrezzo("BUDGET")) * x.getQuantitaVenduta("BUDGET")
    
    return prezzo_budget

def get_costo_tot_consuntivo(list_articoli):
    costo_consuntivo = 0
              
    for x in list_articoli:
        if x.getQuantitaProdotta("CONSUNTIVO") != 0:
            costo_consuntivo += (Decimal(x.getCosto("CONSUNTIVO")) / x.getQuantitaProdotta("CONSUNTIVO") * x.getQuantitaVenduta("CONSUNTIVO"))
    
    return costo_consuntivo

def get_prezzo_tot_consuntivo(list_articoli):
    prezzo_consuntivo = 0
              
    for x in list_articoli:
        prezzo_consuntivo += Decimal(x.getPrezzo("CONSUNTIVO")) * x.getQuantitaVenduta("CONSUNTIVO")
    
    return prezzo_consuntivo
