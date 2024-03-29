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

#BUDGET

def get_costo_produzione_x_art_budget(connection, list_articoli):
        
    sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, (costo_produzione_budget_x_art.C_unit) as costo_unitario from costo_produzione_budget_x_art"
    records = query(connection, sql_select_Query)
    
    for row in records:
        costo_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setCostoProduzione(costo_tot_articolo_budget, "BUDGET")

def get_costo_MP_x_art_budget(connection, list_articoli):
        
    sql_select_Query = "SELECT costo_mp_budget_x_art.codArt, (costo_mp_budget_x_art.costo_unita) as costo_unitario from costo_mp_budget_x_art"
    records = query(connection, sql_select_Query)
    
    for row in records:
        costo_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setCostoMP(costo_tot_articolo_budget, "BUDGET")

def get_prezzo_x_art_budget(connection, list_articoli):

    sql_select_Query = "SELECT vendite_budget_x_art.codArt, sum(vendite_budget_x_art.P_unit*qta)/sum(qta) as P_unit from vendite_budget_x_art group by vendite_budget_x_art.codArt"
    records = query(connection, sql_select_Query)
    
    for row in records:
        prezzo_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setPrezzo(prezzo_tot_articolo_budget, "BUDGET")

def get_quantita_vendute_x_art_budget(connection, list_articoli):
    
    sql_select_Query = "SELECT vendite_budget_x_art.codArt, sum(vendite_budget_x_art.qta) as P_unit from vendite_budget_x_art group by vendite_budget_x_art.codArt"
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaVenduta(quantita_tot_articolo_budget, "BUDGET")

def get_quantita_prodotte_x_art_budget(connection, list_articoli):
    
    sql_select_Query = "SELECT costo_produzione_budget_x_art.codArt, costo_produzione_budget_x_art.qta as P_unit from costo_produzione_budget_x_art "
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_budget = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaProdotta(quantita_tot_articolo_budget, "BUDGET")


def get_costo_produzione_tot_budget(list_articoli):
    costo_budget = 0
                
    for x in list_articoli:
        if x.getQuantitaProdotta("BUDGET") != 0:
            costo_budget += Decimal(x.getCostoProduzione("BUDGET")) / x.getQuantitaProdotta("BUDGET") * x.getQuantitaVenduta("BUDGET")

    return round(costo_budget,3)

def get_costo_MP_tot_budget(list_articoli):
    costo_budget = 0
                
    for x in list_articoli:
        if x.getQuantitaProdotta("BUDGET") != 0:
            costo_budget += Decimal(x.getCostoMP("BUDGET")) / x.getQuantitaProdotta("BUDGET") * x.getQuantitaVenduta("BUDGET")

    return round(costo_budget,3)

def get_prezzo_tot_budget(connection):
    prezzo_budget = 0
              
    sql_select_Query = "SELECT vendite_budget_x_art.qta, vendite_budget_x_art.P_unit from vendite_budget_x_art"
    records = query(connection, sql_select_Query)

    for row in records:
        prezzo_budget += Decimal(row[1])*row[0]
    
    return round(prezzo_budget,3)

def get_quantita_tot_prodotta_budget(list_articoli):
    quantita_budget = 0
              
    for x in list_articoli:
        quantita_budget += x.getQuantitaProdotta("BUDGET")
    
    return quantita_budget

def get_quantita_tot_venduta_budget(list_articoli):
    quantita_budget = 0
              
    for x in list_articoli:
        quantita_budget += x.getQuantitaVenduta("BUDGET")
    
    return quantita_budget

# FINE BUDGET

# CONSUNTIVO

def get_costo_produzione_x_art_consuntivo(connection, list_articoli):

    sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, costo_produzione_consuntivo_x_art.C_unit as costo_unitario from costo_produzione_consuntivo_x_art"
    records = query(connection, sql_select_Query)
    
    for row in records:
        costo_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setCostoProduzione(costo_tot_articolo_consuntivo, "CONSUNTIVO")

def get_costo_MP_x_art_consuntivo(connection, list_articoli):

    sql_select_Query = "SELECT costo_mp_consuntivo_x_art.codArt, costo_mp_consuntivo_x_art.costo_unita as costo_unitario from costo_mp_consuntivo_x_art"
    records = query(connection, sql_select_Query)
    
    for row in records:
        costo_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setCostoMP(costo_tot_articolo_consuntivo, "CONSUNTIVO")

def get_prezzo_x_art_consuntivo(connection, list_articoli):
    
    sql_select_Query = "SELECT vendite_consuntivo_x_art.codArt, sum(vendite_consuntivo_x_art.P_unit*vendite_consuntivo_x_art.qta)/sum(vendite_consuntivo_x_art.qta) as P_unit from vendite_consuntivo_x_art group by vendite_consuntivo_x_art.codArt"
    
    records = query(connection, sql_select_Query)

    for row in records:
        prezzo_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setPrezzo(prezzo_tot_articolo_consuntivo, "CONSUNTIVO")


def get_prezzo_x_art_consuntivo_tassi(connection, list_articoli):

    sql_select_Query = "SELECT vendite_consuntivo_x_art_tassi.codArt, sum(vendite_consuntivo_x_art_tassi.P_unit*vendite_consuntivo_x_art_tassi.qta)/sum(vendite_consuntivo_x_art_tassi.qta) as P_unit from vendite_consuntivo_x_art_tassi group by vendite_consuntivo_x_art_tassi.codArt"

    records = query(connection, sql_select_Query)
    for row in records:
        prezzo_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setPrezzo(prezzo_tot_articolo_consuntivo, "CONSUNTIVOTASSI")

def get_prezzo_tot_consuntivo_tassi(connection):

    prezzo_consuntivo = 0
    sql_select_Query = "SELECT vendite_consuntivo_x_art_tassi.qta, vendite_consuntivo_x_art_tassi.P_unit from vendite_consuntivo_x_art_tassi"    

    records = query(connection, sql_select_Query)
    for row in records:
        prezzo_consuntivo += Decimal(row[1])*row[0]      

    return round(prezzo_consuntivo,3)
        

def get_quantita_vendute_x_art_consuntivo(connection, list_articoli):
    
    sql_select_Query = "SELECT vendite_consuntivo_x_art.codArt, sum(vendite_consuntivo_x_art.qta) as P_unit from vendite_consuntivo_x_art group by vendite_consuntivo_x_art.codArt"
    
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaVenduta(quantita_tot_articolo_consuntivo, "CONSUNTIVO")

def get_quantita_prodotte_x_art_consuntivo(connection, list_articoli):
    
    sql_select_Query = "SELECT costo_produzione_consuntivo_x_art.codArt, costo_produzione_consuntivo_x_art.qta as P_unit from costo_produzione_consuntivo_x_art "
    records = query(connection, sql_select_Query)

    for row in records:
        quantita_tot_articolo_consuntivo = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaProdotta(quantita_tot_articolo_consuntivo, "CONSUNTIVO")


def get_costo_MP_tot_consuntivo(list_articoli):
    costo_consuntivo = 0
            
    for x in list_articoli:
        if x.getQuantitaProdotta("CONSUNTIVO") != 0:
            costo_consuntivo += (Decimal(x.getCostoMP("CONSUNTIVO")) / x.getQuantitaProdotta("CONSUNTIVO") * x.getQuantitaVenduta("CONSUNTIVO"))
            
    return round(costo_consuntivo,3)

def get_costo_produzione_tot_consuntivo(list_articoli):
    costo_consuntivo = 0
            
    for x in list_articoli:
        if x.getQuantitaProdotta("CONSUNTIVO") != 0:
            costo_consuntivo += (Decimal(x.getCostoProduzione("CONSUNTIVO")) / x.getQuantitaProdotta("CONSUNTIVO") * x.getQuantitaVenduta("CONSUNTIVO"))
            
    return round(costo_consuntivo,3)

def get_prezzo_tot_consuntivo(connection):
    prezzo_consuntivo = 0
    
    sql_select_Query = "SELECT vendite_consuntivo_x_art.qta, vendite_consuntivo_x_art.P_unit from vendite_consuntivo_x_art"    
    records = query(connection, sql_select_Query)

    for row in records:
        prezzo_consuntivo += Decimal(row[1])*row[0]
        
    return round(prezzo_consuntivo,3)

def get_quantita_tot_prodotta_consuntivo(list_articoli):
    quantita_consuntivo = 0
              
    for x in list_articoli:
        quantita_consuntivo += x.getQuantitaProdotta("CONSUNTIVO")
    
    return quantita_consuntivo

def get_quantita_tot_venduta_consuntivo(list_articoli):
    quantita_consuntivo = 0
              
    for x in list_articoli:
        quantita_consuntivo += x.getQuantitaVenduta("CONSUNTIVO")
    
    return quantita_consuntivo

# FINE CONSUNTIVO

# STANDARD

def get_mix_std(connection, list_articoli):
    
    sql_select_Query = "SELECT mix_x_art_budget.codArt, mix_x_art_budget.val FROM mix_x_art_budget"
    records = query(connection, sql_select_Query)

    for row in records:
        mix = row[1]
        art = amongUs(list_articoli, row[0])
        art.setMix(mix, "STANDARD")

def set_quantita_prodotte_x_art_std(list_articoli):

    for art in list_articoli:
        qta = art.getMix("STANDARD") * get_quantita_tot_prodotta_consuntivo(list_articoli)
        art.setQuantitaProdotta(qta, "STANDARD")

def set_quantita_vendute_x_art_std(connection, list_articoli):
    
    sql_select_Query = "SELECT mix_standard.codArt, sum(mix_standard.qta) FROM mix_standard group by mix_standard.codArt"
    records = query(connection, sql_select_Query)

    for row in records:
        qta = row[1]
        art = amongUs(list_articoli, row[0])
        art.setQuantitaVenduta(qta, "STANDARD")

def get_costo_produzione_tot_std(list_articoli):
    costo_std = 0
              
    for x in list_articoli:
        if x.getQuantitaProdotta("BUDGET") != 0:
            costo_std += Decimal(x.getCostoProduzione("BUDGET")) / x.getQuantitaProdotta("BUDGET") * x.getQuantitaVenduta("STANDARD")
    return round(costo_std,3)

def get_costo_MP_tot_std(list_articoli):
    costo_std = 0
              
    for x in list_articoli:
        if x.getQuantitaProdotta("BUDGET") != 0:
            costo_std += Decimal(x.getCostoMP("BUDGET")) / x.getQuantitaProdotta("BUDGET") * x.getQuantitaVenduta("STANDARD")
    return round(costo_std,3)

def get_prezzo_tot_std(connection):
    prezzo_std = 0
              
    sql_select_Query = "SELECT mix_standard.qta, mix_standard.P_unit from mix_standard"
    records = query(connection, sql_select_Query)

    for row in records:
        prezzo_std += Decimal(row[1])*row[0]
    
    return round(prezzo_std,3)

# FINE STANDARD

# EFFETTIVO

def get_mix_eff(connection, list_articoli):
    
    sql_select_Query = "SELECT mix_x_art_consuntivo.codArt, mix_x_art_consuntivo.val FROM mix_x_art_consuntivo"
    records = query(connection, sql_select_Query)

    for row in records:
        mix = row[1]
        art = amongUs(list_articoli, row[0])
        art.setMix(mix, "EFFETTIVO")

def set_quantita_prodotte_x_art_eff(list_articoli):
    
    for art in list_articoli:
        qta = art.getMix("EFFETTIVO") * get_quantita_tot_prodotta_consuntivo(list_articoli)
        art.setQuantitaProdotta(qta, "EFFETTIVO")

def set_quantita_vendute_x_art_eff(connection, list_articoli):
    
        sql_select_Query = "SELECT mix_effettivo.codArt, sum(mix_effettivo.qta) FROM mix_effettivo group by mix_effettivo.codArt"
        records = query(connection, sql_select_Query)

        for row in records:
            qta = row[1]
            art = amongUs(list_articoli, row[0])
            art.setQuantitaVenduta(qta, "EFFETTIVO")

  
def get_costo_produzione_tot_eff(list_articoli):   
    costo_eff = 0
              
    for x in list_articoli:
        if x.getQuantitaProdotta("BUDGET") != 0:
            costo_eff += Decimal(x.getCostoProduzione("BUDGET")) / x.getQuantitaProdotta("BUDGET") * x.getQuantitaVenduta("EFFETTIVO") 
    
    return round(costo_eff,3)

def get_costo_MP_tot_eff(list_articoli):   
    costo_eff = 0
              
    for x in list_articoli:
        if x.getQuantitaProdotta("BUDGET") != 0:
            costo_eff += Decimal(x.getCostoMP("BUDGET")) / x.getQuantitaProdotta("BUDGET") * x.getQuantitaVenduta("EFFETTIVO") 
    
    return round(costo_eff,3)

def get_prezzo_tot_eff(connection):
    prezzo_eff = 0
              
    sql_select_Query = "SELECT mix_effettivo.qta, mix_effettivo.P_unit from mix_effettivo"
    records = query(connection, sql_select_Query)

    for row in records:
        prezzo_eff += Decimal(row[1])*row[0]
    
    return round(prezzo_eff,3)
    
# FINE EFFETTIVO

# SCOSTAMENTO

def set_scostamento_volume(list_articoli):

    delta_p = 0
    delta_c = 0
    delta_m = 0
    p_bdg = 0
    p_std = 0
    c_bdg = 0
    c_std = 0

    for art in list_articoli:
        p_std = (art.getPrezzo("BUDGET")*art.getQuantitaVenduta("STANDARD"))
        p_bdg = (art.getPrezzo("BUDGET")*art.getQuantitaVenduta("BUDGET"))
        if art.getQuantitaProdotta("BUDGET") != 0:
            c_std = (Decimal(art.getCostoMP("BUDGET") + art.getCostoProduzione("BUDGET")) / art.getQuantitaProdotta("BUDGET") * art.getQuantitaVenduta("STANDARD")) 
            c_bdg = (Decimal(art.getCostoMP("BUDGET") + art.getCostoProduzione("BUDGET")) / art.getQuantitaProdotta("BUDGET") * art.getQuantitaVenduta("BUDGET")) 
        delta_p = (p_std - p_bdg) 
        delta_c = (c_std - c_bdg)
        delta_m = delta_p - delta_c

        art.setDeltaVolume(delta_p, delta_c, delta_m)

def set_scostamento_mix(list_articoli):

    delta_p = 0
    delta_c = 0
    delta_m = 0
    p_eff = 0
    p_std = 0
    c_eff = 0
    c_std = 0

    for art in list_articoli:
        p_std = (art.getPrezzo("BUDGET")*art.getQuantitaVenduta("STANDARD"))
        p_eff = (art.getPrezzo("BUDGET")*art.getQuantitaVenduta("EFFETTIVO"))
        if art.getQuantitaProdotta("BUDGET") != 0:
            c_std = (Decimal(art.getCostoMP("BUDGET") + art.getCostoProduzione("BUDGET")) / art.getQuantitaProdotta("BUDGET") * art.getQuantitaVenduta("STANDARD")) 
            c_eff= (Decimal(art.getCostoMP("BUDGET") + art.getCostoProduzione("BUDGET")) / art.getQuantitaProdotta("BUDGET") * art.getQuantitaVenduta("EFFETTIVO")) 
        delta_p = (p_eff - p_std) 
        delta_c = (c_eff - c_std)
        delta_m = delta_p - delta_c

        art.setDeltaMix(delta_p, delta_c, delta_m)
        
def set_scostamento_prezzo_costo(list_articoli):

    delta_p = 0
    delta_c = 0
    delta_m = 0
    p_eff = 0
    p_pc = 0
    c_eff = 0
    c_pc = 0

    for art in list_articoli:
        p_pc = (art.getPrezzo("CONSUNTIVO")*art.getQuantitaVenduta("CONSUNTIVO"))
        p_eff = (art.getPrezzo("BUDGET")*art.getQuantitaVenduta("EFFETTIVO"))
        if art.getQuantitaProdotta("CONSUNTIVO") != 0:
            c_pc = (Decimal(art.getCostoMP("CONSUNTIVO") + art.getCostoProduzione("CONSUNTIVO")) / art.getQuantitaProdotta("CONSUNTIVO") * art.getQuantitaVenduta("CONSUNTIVO")) 
        if art.getQuantitaProdotta("BUDGET") != 0:
            c_eff= (Decimal(art.getCostoMP("BUDGET") + art.getCostoProduzione("BUDGET")) / art.getQuantitaProdotta("BUDGET") * art.getQuantitaVenduta("EFFETTIVO")) 
        delta_p = (p_pc - p_eff) 
        delta_c = (c_pc - c_eff)
        delta_m = delta_p - delta_c

        art.setDeltaPrezzoCosto(delta_p, delta_c, delta_m)



# FINE SCOSTAMENTO
