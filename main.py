import mysql.connector
from mysql.connector import Error
from model_utils.articolo import Articolo

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sistemi_controllo_gestione',
                                         user='root',
                                         password='')
    if connection.is_connected():

        list_articoli = []

        quantita_budget = 0
        costo_budget = 0
        prezzo_budget = 0

        quantita_consuntivo = 0
        costo_consuntivo = 0
        prezzo_consuntivo = 0

        quantita_mix_std = 0
        costo_mix_std = 0
        prezzo_mix_std = 0

        quantita_mix_eff = 0
        costo_mix_eff = 0
        prezzo_mix_eff = 0
               
        # def amongUs(codArt):
        #     for art in list_articoli:
        #         if art.codArt == codArt:
        #             return self.art

        # # 0C    COSTO UNITARIO PER ARTICOLO BUDGET
        # sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, costo_produzione_budget_x_art.C_unit as costo_unitario_produzione, costo_mp_budget_x_art.costo_unita as costo_unitario_mp from costo_produzione_budget_x_art, costo_mp_budget_x_art where costo_produzione_budget_x_art.codArt = costo_mp_budget_x_art.codArt GROUP by costo_produzione_budget_x_art.codArt LIMIT 1"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     art = Articolo(row[0])
        #     costo_tot_articolo_budget = row[1]
        #     art.setCosto(costo_tot_articolo_budget, 0)
        #     list_articoli.append(art)
        
        # # 0P    RICAVI UNITARIO PER ARTICOLO BUDGET  
        # sql_select_Query = "SELECT vendite_budget_x_art.Codice_articolo, vendite_budget_x_art.Prezzo_unita FROM vendite_budget_x_art LIMIT 1"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     prezzo_tot_articolo_budget = row[1]
        #     x = amongUs(row[0])
        #     x.setPrezzo(prezzo_tot_articolo_budget, 0)

        # # 0Q    QUANTITA PER ARTICOLO BUDGET
        # sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, costo_produzione_budget_x_art.qta from costo_produzione_budget_x_art LIMIT 1"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     quantita_articolo_budget = row[1]
        #     x = amongUs(row[0])
        #     x.setQuantita(quantita_articolo_budget, 0)

        # # 3C    COSTO UNITARIO PER ARTICOLO CONSUNTIVO
        # sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, costo_produzione_consuntivo_x_art.C_unit as costo_unitario_produzione, costo_mp_budget_x_art.costo_unita as costo_unitario_mp from costo_produzione_consuntivo_x_art, costo_mp_budget_x_art where costo_produzione_consuntivo_x_art.codArt = costo_mp_budget_x_art.codArt GROUP by costo_produzione_consuntivo_x_art.codArt LIMIT 1"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_tot_articolo_consuntivo = row[1] #+row[2]
        #     x = amongUs(row[0])
        #     x.setCosto(costo_tot_articolo_consuntivo, 1)

        # # 3P    RICAVI UNITARIO PER ARTICOLO CONSUNTIVO  
        # sql_select_Query = "SELECT vendite_consuntivo_x_art.Codice_articolo, vendite_consuntivo_x_art.Prezzo_unita FROM vendite_consuntivo_x_art LIMIT 1"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     prezzo_tot_articolo_consuntivo = row[1]
        #     x = amongUs(row[0])
        #     x.setPrezzo(prezzo_tot_articolo_consuntivo, 1)
        
        # # 3Q    QUANTITA PER ARTICOLO CONSUNTIVO
        # sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, costo_produzione_consuntivo_x_art.qta from costo_produzione_consuntivo_x_art LIMIT 1"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     quantita_articolo_consuntivo = row[1]
        #     x = amongUs(row[0])
        #     x.setQuantita(quantita_articolo_consuntivo, 1)

        # # PREZZO   TOT BUDGET - CONSUNTIVO
        # # COSTO    TOT BUDGET - CONSUNTIVO
        # # QUANTITA TOT BUDGET - CONSUNTIVO
        # for x in list_articoli:
        #     prezzo_budget += x.getPrezzo(0)
        #     prezzo_consuntivo += x.getPrezzo(3)
        #     costo_budget += x.getPrezzo(0)
        #     costo_consuntivo += x.getPrezzo(3)
        #     quantita_budget += x.quantitaBudget
        #     quantita_consuntivo += x.quantitaConsuntivo

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")


def get_tot_budget(connection):
    costo_budget = 0
    
    if connection.is_connected():
        list_articoli = []
        sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, costo_produzione_budget_x_art.C_unit as costo_unitario_produzione, costo_mp_budget_x_art.costo_unita as costo_unitario_mp from costo_produzione_budget_x_art, costo_mp_budget_x_art where costo_produzione_budget_x_art.codArt = costo_mp_budget_x_art.codArt GROUP by costo_produzione_budget_x_art.codArt LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            art = Articolo(row[0])
            costo_tot_articolo_budget = row[1]
            art.setCosto(costo_tot_articolo_budget, 0)
            list_articoli.append(art)
            
        for x in list_articoli:
            costo_budget += x.getCosto(0)
    
    return costo_budget

