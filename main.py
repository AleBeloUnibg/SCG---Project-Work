import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sistemi_controllo_gestione',
                                         user='root',
                                         password='')
    if connection.is_connected():

        prezzo_budget = 0
        prezzo_consuntivo = 0
        prezzo_mix_std = 0
        prezzo_mix_eff = 0
        costo_budget = 0
        costo_consuntivo = 0
        costo_mix_std = 0
        costo_mix_eff = 0
        quantita_tot_budget = 0
        quantita_tot_consuntivo = 0
        
        mix_articolo = 0

        prezzo_mix_std = 0
        costo_mix_std = 0
        prezzo_mix_eff = 0
        costo_mix_eff = 0

        costo_tot_articolo_budget = []
        prezzo_tot_articolo_budget = []
        quantita_tot_articolo_budget = []
        
        costo_tot_articolo_mix_std = []
        prezzo_tot_articolo_mix_std = []
        quantita_tot_articolo_mix_std = []

        costo_tot_articolo_mix_eff = []
        prezzo_tot_articolo_mix_eff = []
        quantita_tot_articolo_mix_eff = []
        quantita_tot_articolo_mix_std = []

        costo_tot_articolo_consuntivo = []
        prezzo_tot_articolo_consuntivo = []
        quantita_tot_articolo_consuntivo = []
        
        list_articoli = []
        
        # TOTALE PREZZO BUDGET
        sql_select_Query = "SELECT SUM(vendite_budget.Importo_tot) FROM vendite_budget"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            prezzo_budget = row[0]

        # TOTALE PREZZO CONSUNTIVO
        sql_select_Query = "SELECT SUM(vendite_consuntivo.Importo_tot) FROM vendite_consuntivo"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            prezzo_consuntivo = row[0]
        
        # SCOSTAMENTO TOTALE            
        # print("Scostamento totale = ", (prezzo_consuntivo-prezzo_budget))

        # COSTO UNITARIO PER ARTICOLO BUDGET
        sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, costo_produzione_budget_x_art.C_unit as costo_unitario_produzione, costo_mp_budget_x_art.costo_unita as costo_unitario_mp from costo_produzione_budget_x_art, costo_mp_budget_x_art where costo_produzione_budget_x_art.codArt = costo_mp_budget_x_art.codArt GROUP by costo_produzione_budget_x_art.codArt LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            costo_tot_articolo_budget = row[1]+row[2]
            print("codArt = ", row[0])
            print("costo_tot_articolo_budget = ", costo_tot_articolo_budget)

        # RICAVI UNITARIO PER ARTICOLO BUDGET  
        sql_select_Query = "SELECT vendite_budget_x_art.Codice_articolo, vendite_budget_x_art.Prezzo_unita FROM vendite_budget_x_art LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            prezzo_tot_articolo_budget = row[1]
            print("codArt = ", row[0])
            print("prezzo_tot_articolo_budget = ", prezzo_tot_articolo_budget)
        
        # COSTO UNITARIO PER ARTICOLO CONSUNTIVO
        sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, costo_produzione_consuntivo_x_art.C_unit as costo_unitario_produzione, costo_mp_budget_x_art.costo_unita as costo_unitario_mp from costo_produzione_consuntivo_x_art, costo_mp_budget_x_art where costo_produzione_consuntivo_x_art.codArt = costo_mp_budget_x_art.codArt GROUP by costo_produzione_consuntivo_x_art.codArt LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            costo_tot_articolo_consuntivo = row[1]+row[2]
            print("codArt = ", row[0])
            print("costo_tot_articolo_consuntivo = ", costo_tot_articolo_consuntivo)

        # RICAVI UNITARIO PER ARTICOLO CONSUNTIVO  
        sql_select_Query = "SELECT vendite_consuntivo_x_art.Codice_articolo, vendite_consuntivo_x_art.Prezzo_unita FROM vendite_consuntivo_x_art LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            prezzo_tot_articolo_consuntivo = row[1]
            print("codArt = ", row[0])
            print("prezzo_tot_articolo_consuntivo = ", prezzo_tot_articolo_consuntivo)
        
        # QUANTITA PER ARTICOLO BUDGET
        sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, costo_produzione_budget_x_art.qta from costo_produzione_budget_x_art LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            quantita_tot_articolo_budget = row[1]
            print("codArt = ", row[0])
            print("quantita_tot_articolo_budget = ", quantita_tot_articolo_budget)
        
        # QUANTITA PER ARTICOLO CONSUNTIVO
        sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, costo_produzione_consuntivo_x_art.qta from costo_produzione_consuntivo_x_art LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            quantita_tot_articolo_consuntivo = row[1]
            print("codArt = ", row[0])
            print("quantita_tot_articolo_consuntivo = ", quantita_tot_articolo_consuntivo)

        # QUANTITA BUDGET
        sql_select_Query = "SELECT sum(costo_produzione_consuntivo_x_art.qta) from costo_produzione_consuntivo_x_art" 
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            quantita_tot_budget = row[0]
            print("quantita_tot_budget = ", quantita_tot_budget)

        # MIX PER ARTICOLO BUDGET
        sql_select_Query = "SELECT mix_x_art_budget.codArt, mix_x_art_budget.val from mix_x_art_budget LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            mix_articolo = row[1]
            print("mix_articolo = ", mix_articolo)

        # QUANTITA CONSUNTIVO
        sql_select_Query = "SELECT sum(vendite_consuntivo.Quantita) from vendite_consuntivo"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            quantita_tot_consuntivo = row[0]
            print("quantita_tot_consuntivo = ", quantita_tot_consuntivo)

        quantita_tot_articolo_mix_std = quantita_tot_consuntivo * mix_articolo
        print("quantita_tot_articolo_mix_std = ", quantita_tot_articolo_mix_std)

        # CALCOLO IL MARGINE DI CONTRIBUZIONE
        mdc_budget = prezzo_tot_articolo_budget - costo_tot_articolo_budget
        
        # prezzo_mix_std = quantita_tot_articolo_mix_std * prezzo_tot_articolo_budget
        # costo_mix_std = quantita_tot_articolo_mix_std * costo_tot_articolo_budget


        
        # # COSTO TOTALE DI TUTTE LE VENDITE
        # sql_select_Query = "SELECT sum(vendite_budget.Quantita * totale_costo) as costo_totale from vendite_budget INNER join (select codArt, sum(costoProd) as totale_costo from costo_produzione_budget_x_art group by codArt) as test on vendite_budget.codArt = test.codArt"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_budget = row[0]

        # # QUANTITA TOTALE 
        # sql_select_Query = "SELECT sum(vendite_budget.Quantita * totale_costo) as costo_totale from vendite_budget INNER join (select codArt, sum(costoProd) as totale_costo from costo_produzione_budget_x_art group by codArt) as test on vendite_budget.codArt = test.codArt"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_budget = row[0]
        
        # # COSTI TOTALI BUDGET  
        # sql_select_Query = "SELECT sum(costo_produzione_budget_x_art.costoProd) FROM costo_produzione_budget_x_art"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_budget = row[0]
        
        # mol_budget = prezzo_budget - costo_budget
        # print("MOL budget", prezzo_budget - costo_budget)

        # # RICAVI TOTALI CONSUNTIVO  
        # sql_select_Query = "SELECT sum(vendite_CONSUNTIVO_x_art.P) FROM vendite_CONSUNTIVO_x_art"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     prezzo_CONSUNTIVO = row[0]
        
        # # COSTI TOTALI CONSUNTIVO  
        # sql_select_Query = "SELECT sum(costo_CONSUNTIVO_x_art.costoProd) FROM costo_CONSUNTIVO_x_art"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_CONSUNTIVO = row[0]
        
        # mol_consuntivo = prezzo_CONSUNTIVO - costo_CONSUNTIVO
        # print("MOL CONSUNTIVO", prezzo_CONSUNTIVO - costo_CONSUNTIVO)
        # print("")

        # print("SCOSTAMENTO", mol_consuntivo - mol_budget)
        # print("")

        # # RICAVI TOTALI MIX STANDARD  
        # sql_select_Query = "SELECT sum(mix_standard.qta * vendite_budget_x_art.P_unit) FROM mix_standard INNER JOIN vendite_budget_x_art On vendite_budget_x_art.codArt = mix_standard.codArt"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     prezzo_mix_std = row[0]

        # # COSTI TOTALI MIX STANDARD  
        # sql_select_Query = "SELECT sum(mix_standard.qta * costo_produzione_budget_x_art.C_unit) FROM mix_standard INNER JOIN costo_produzione_budget_x_art on costo_produzione_budget_x_art.codArt = mix_standard.codArt"    
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_mix_std = row[0]

        # print("Prezzo MIX STANDARD", prezzo_mix_std )
        # print("Costo MIX STANDARD", costo_mix_std)
        # print("MOL MIX STANDARD", prezzo_mix_std - costo_mix_std)
        # print("")

        # # RICAVI TOTALI MIX EFFETTIVO  
        # sql_select_Query = "SELECT sum(vendite_consuntivo_x_art.qta * vendite_budget_x_art.P_unit) FROM vendite_consuntivo_x_art INNER JOIN vendite_budget_x_art On vendite_budget_x_art.codArt = vendite_consuntivo_x_art.codArt"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     prezzo_mix_eff = row[0]

        # # COSTI TOTALI MIX EFFETTIVO  
        # sql_select_Query = "SELECT sum(vendite_consuntivo_x_art.qta * costo_produzione_budget_x_art.C_unit) FROM vendite_consuntivo_x_art INNER JOIN costo_produzione_budget_x_art on costo_produzione_budget_x_art.codArt = vendite_consuntivo_x_art.codArt"    
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_mix_eff = row[0]

        # print("Prezzo MIX EFFETTIVO", prezzo_mix_eff )
        # print("Costo MIX EFFETTIVO", costo_mix_eff)
        # print("MOL MIX EFFETTIVO", prezzo_mix_eff - costo_mix_eff)
        # print("")


        # uno = (prezzo_mix_std - costo_mix_std) - (prezzo_budget - costo_budget)
        # print(uno)
        # print("")
        # due = (prezzo_mix_eff - costo_mix_eff) - (prezzo_mix_std - costo_mix_std)
        # print(due)
        # print("")
        # tre = (prezzo_CONSUNTIVO - costo_CONSUNTIVO) - (prezzo_mix_eff - costo_mix_eff)
        # print(tre)
        # print("")

        # #BUDGET STD
        # sql_select_Query = "SELECT costi_impiego_area_budget.codArea, sum(costi_impiego_area_budget.costo)* sum(costi_impiego_area_budget.tempo)* sum(costi_impiego_area_budget.qta) from costi_impiego_area_budget GROUP by costi_impiego_area_budget.codArea"    
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_mix_eff = row[0]

        # #MIX STD
        # sql_select_Query = "SELECT costi_impiego_area_budget.codArea, sum(costi_impiego_area_budget.costo)* sum(costi_impiego_area_budget.tempo)* sum(costi_impiego_area_budget.qta) from costi_impiego_area_budget GROUP by costi_impiego_area_budget.codArea"    
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_mix_eff = row[0]

        # #BUDGET EFFETTIVO
        # sql_select_Query = "SELECT costi_impiego_area_consuntivo.codArea, sum(costi_impiego_area_consuntivo.costo)* sum(costi_impiego_area_consuntivo.tempo)* sum(costi_impiego_area_consuntivo.qta) from costi_impiego_area_consuntivo GROUP by costi_impiego_area_consuntivo.codArea"    
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # records = cursor.fetchall()
        # for row in records:
        #     costo_mix_eff = row[0]

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

