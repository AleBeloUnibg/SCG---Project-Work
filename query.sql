# associare ad ogni cliente il relativo tasso di cambio
CREATE VIEW Cliente_Tax (codCli, codPag, valuta, tassoCambio, bud_cons) AS
SELECT Codice_cliente, Cod_condizioni_pagamento, clienti.Codice_valuta, Tasso_cambio_medio, Budget_consuntivo
FROM clienti, tassi_di_cambio
WHERE clienti.Codice_valuta = tassi_di_cambio.Codice_valuta

# associare ogni cliente con il tasso di cambio la sua vendita
CREATE VIEW Cliente_Adj (codCli, codPag, valuta, tassoCambio, budget_cons, Nr_articolo, Quantita, importo_tot) AS
SELECT codCli, codPag, valuta, tassoCambio, budget_consuntivo, Nr_articolo, Quantita, Importo_vendita
FROM vendita, Cliente_Tax
WHERE Nr_origine = codCli AND  Cliente_Tax.bud_cons = 0

# estrazione/separazione in tabella VenditeBudget.csv e VenditeConsuntivo.csv
CREATE VIEW Vendite_Budget(codCli, codPag, valuta, tassoCambio, codArt, Quantita, importo_tot) AS
SELECT codCli, codPag, valuta, tassoCambio, Nr_articolo, Quantita, importo_tot
FROM Cliente_Adj
WHERE budget_cons = 0

CREATE VIEW Vendite_Consuntivo(codCli, codPag, valuta, tassoCambio, codArt, Quantita, importo_tot) AS
SELECT codCli, codPag, valuta, tassoCambio, Nr_articolo, Quantita, importo_tot
FROM Cliente_Adj
WHERE budget_cons = 1

# dividere per il tasso di cambio (sia in VenditeBudget.csv che in VenditeConsuntivo.csv)
CREATE VIEW Vendite_Budget_X_art(codArt, qta, P_unit) AS
SELECT codArt, Quantita AS qta, Importo_tot/(Quantita*tassoCambio) AS P_unit
FROM Vendite_Budget
WHERE Quantita != 0

CREATE VIEW Vendite_Consuntivo_X_art(codArt, qta, P_unit) AS
SELECT codArt, Quantita AS qta, Importo_tot/(Quantita*tassoCambio) AS P_unit
FROM Vendite_Consuntivo
WHERE Quantita != 0

# unisce l impiego dell articolo all equivalente costo orario di produzione (sia a Budget che a Consuntivo)
CREATE VIEW Impiego_Costo_Risorse_Budget(codArt, codOrd, area, codArea, risorsa, t, q, costoH) AS
SELECT Nr_articolo, Nr_ordine_produzione, Descrizione, I.Nr_Area_produzione, I.Risorsa, Tempo_risorsa, Quantita_output, Costo_orario
FROM impiego_orario_risorse AS I, costo_orario_risorse_budget AS C
WHERE I.Risorsa = C.Risorsa AND I.Nr_area_produzione = C.Area_produzione AND budget_consuntivo = 0

CREATE VIEW Impiego_Costo_Risorse_Consuntivo(codArt, codOrd, area, codArea, risorsa, t, q, costoH) AS
SELECT Nr_articolo, Nr_ordine_produzione, Descrizione, I.Nr_Area_produzione, I.Risorsa, Tempo_risorsa, Quantita_output, Costo_orario
FROM impiego_orario_risorse AS I, costo_orario_risorse_consuntivo AS C
WHERE I.Risorsa = C.Risorsa AND I.Nr_area_produzione = C.Area_produzione AND budget_consuntivo = 1

# distinzione nelle tre aree Articolo - Ordine di produzione - Area
CREATE VIEW Costo_produzione_Budget_X_art(codArt, C_unit, qta) AS
SELECT codArt, sum(C_unit), sum(qta)
FROM   (SELECT codArt, sum(Costo_totale) AS C_unit, qta, a.codOrd
		FROM(	SELECT codArt, Area , sum(t)*costoH AS Costo_totale, sum(q) AS qta, codOrd
				FROM Impiego_Costo_Risorse_Budget
				GROUP BY codArt, codOrd, area) AS a
		GROUP BY a.codArt, a.codOrd) AS a1
GROUP BY a1.codArt

CREATE VIEW Costo_produzione_Consuntivo_X_art(codArt, C_unit, qta) AS
SELECT a1.CodArt, sum(C_unit), sum(qta)
FROM   (SELECT a.CodArt, sum(Costo_totale) AS C_unit, qta, a.codOrd
		FROM(	SELECT CodArt, Area , sum(t)*costoH AS Costo_totale, sum(q) AS qta, codOrd
				FROM Impiego_Costo_Risorse_Consuntivo
				GROUP BY CodArt, codOrd, Area) AS a
		GROUP BY a.CodArt, a.codOrd) AS a1
GROUP BY a1.CodArt

'
# calcolo tabella impiegoCostoOrarioRisorseBudget
#CREATE VIEW Costi_impiego_area_budget(area, codArea, costo, tempo, qta) AS
#SELECT area, codArea, sum(costoH), sum(t), sum(q)
#FROM Impiego_Costo_Risorse_Budget
#GROUP BY area
#
## calcolo tabella impiegoCostoOrarioRisorseConsuntivo
#CREATE VIEW Costi_impiego_area_consuntivo(area, codArea, costo, tempo, qta) AS
#SELECT area, codArea, sum(costoH), sum(t), sum(q)
#FROM Impiego_Costo_Risorse_Consuntivo
#GROUP BY area
'

# tabelle contenenti le Quantita prodotte per ogni ordine di produzione di un dato articolo
CREATE VIEW Impiego_tmp_budget(codArt, OdP, q) AS
SELECT codArt, a.codOrd, qta
FROM(	SELECT codArt, Area , sum(q) AS qta, codOrd
		FROM Impiego_Costo_Risorse_Budget
		GROUP BY codArt, codOrd, area) AS a
GROUP BY a.codArt, a.codOrd

CREATE VIEW Impiego_tmp_consuntivo(codArt, OdP, q) AS 
SELECT codArt, a.codOrd, qta 
FROM( SELECT codArt, area , sum(q) AS qta, codOrd 
	FROM Impiego_Costo_Risorse_Consuntivo 
	GROUP BY codArt, codOrd, area) AS a 
GROUP BY a.codArt, a.codOrd;

CREATE VIEW Consumi_tmp(codArt, budg_cons, OdP, importo) AS
SELECT Nr_Articolo, Budget_consuntivo, Nr_documento, sum(Importo_costo) as Importo_costo 
FROM consumi 
WHERE Nr_Articolo NOT IN (SELECT _riutilizzati.Codice_MP from _riutilizzati) 
GROUP BY Nr_Articolo, Nr_documento

# collegamento OdP consumi-impieghi
CREATE VIEW Costo_MP_budget_x_art(codArt, qta, costo_unita)AS
SELECT codArt, sum(q), sum(costo_unita) as costo_unita
FROM (SELECT i.codArt, i.OdP, q, importo as costo_unita
		FROM consumi_tmp AS c, impiego_tmp_budget AS i
		WHERE c.OdP = i.OdP AND c.codArt = i.codArt AND c.budg_cons = 0) AS a
GROUP BY a.codArt

CREATE VIEW Costo_MP_consuntivo_x_art(codArt, qta, costo_unita)AS
SELECT codArt, sum(q), sum(costo_unita) as costo_unita
FROM (SELECT i.codArt, i.OdP, q, importo as costo_unita
		FROM consumi_tmp AS c, impiego_tmp_consuntivo AS i
		WHERE c.OdP = i.OdP AND c.codArt = i.codArt AND c.budg_cons = 1) AS a
GROUP BY a.codArt

# calcolo mix produttivo per articolo
CREATE VIEW Mix_X_art_budget(codArt, val) AS
SELECT codArt, sum(Quantita)/(SELECT sum(Quantita)
									   FROM Vendite_Budget) 
FROM Vendite_Budget
GROUP BY codArt

CREATE VIEW Mix_X_art_consuntivo(codArt, val) AS
SELECT codArt, sum(Quantita)/(SELECT sum(Quantita)
					FROM Vendite_Consuntivo) 
FROM Vendite_Consuntivo
GROUP BY codArt

# calcolo Quantita mixStandard
CREATE VIEW Mix_standard(codArt, qta, P_unit) AS
SELECT codArt, qta/(SELECT sum(qta) FROM Vendite_budget_X_art)*(SELECT sum(qta) FROM Vendite_Consuntivo_X_art), P_unit
FROM Vendite_Budget_X_art

CREATE VIEW _Prezzo_eff(codArt, P_unit) AS
SELECT codArt, sum(P_unit*qta)/sum(qta)
FROM Vendite_Budget_X_art
GROUP BY codArt

CREATE VIEW _Quantita_eff(codArt, qta) AS
SELECT codArt, sum(qta/(SELECT sum(qta) FROM Vendite_consuntivo_X_art)*(SELECT sum(qta) FROM Vendite_Consuntivo_X_art)) 
FROM Vendite_consuntivo_X_art 
GROUP BY codArt
	
# calcolo Quantita mixEffettivo
CREATE VIEW Mix_effettivo(codArt, qta, P_unit) AS
SELECT q.codArt, q.qta, p.P_unit
FROM _Prezzo_eff as p join _Quantita_eff as q on p.codArt=q.codArt





