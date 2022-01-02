from decimal import Decimal

class Articolo:
    def __init__(self, codArt):
        self.codArt = codArt
        self.prezzoBudget = 0
        self.prezzoStandard = 0
        self.prezzoEffettivo = 0
        self.prezzoConsuntivo = 0
        self.costoProduzioneBudget = 0
        self.costoMPBudget = 0
        self.costoProduzioneStandard = 0
        self.costoMPStandard = 0
        self.costoProduzioneEffettivo = 0
        self.costoMPEffettivo = 0
        self.costoProduzioneConsuntivo = 0
        self.costoMPConsuntivo = 0
        self.quantitaBudgetProdotta = 0
        self.quantitaStandardProdotta = 0
        self.quantitaEffettivoProdotta = 0
        self.quantitaConsuntivoProdotta = 0
        self.quantitaBudgetVenduta = 0
        self.quantitaStandardVenduta = 0
        self.quantitaEffettivoVenduta = 0
        self.quantitaConsuntivoVenduta = 0
        self.quantitaStandardVenduta = 0
        self.mixSTD = 0
        self.mixEFF = 0
    
    def getCodice(self):
        return self.codArt

    def setPrezzo(self, p, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                self.prezzoBudget = p
                self.prezzoStandard = p
                self.prezzoEffettivo = p
            elif budget_consuntivo == "CONSUNTIVO":
                self.prezzoConsuntivo = p
    
    def getPrezzo(self, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                return round(self.prezzoBudget, 3)
            elif budget_consuntivo == "STANDARD":
                return round(self.prezzoStandard,3)
            elif budget_consuntivo == "EFFETTIVO":
                return round(self.prezzoEffettivo,3)
            elif budget_consuntivo == "CONSUNTIVO":
                return round(self.prezzoConsuntivo,3)

    def setCostoProduzione(self, c, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                self.costoProduzioneBudget = c
                self.costoProduzioneStandard = c
                self.costoProduzioneEffettivo = c
            elif budget_consuntivo == "CONSUNTIVO":
                self.costoProduzioneConsuntivo = c
    
    def getCostoProduzione(self, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                return round (Decimal(self.costoProduzioneBudget),3)
            elif budget_consuntivo == "STANDARD":
                return round (Decimal(self.costoProduzioneStandard),3)
            elif budget_consuntivo == "EFFETTIVO":
                return round (Decimal(self.costoProduzioneEffettivo),3)
            elif budget_consuntivo == "CONSUNTIVO":
                return round (Decimal(self.costoProduzioneConsuntivo), 3)

    def setCostoMP(self, c, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                self.costoMPBudget = c
                self.costoMPStandard = c
                self.costoMPEffettivo = c
            elif budget_consuntivo == "CONSUNTIVO":
                self.costoMPConsuntivo = c
    
    def getCostoMP(self, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                return round (Decimal(self.costoMPBudget),3)
            elif budget_consuntivo == "STANDARD":
                return round (Decimal(self.costoMPStandard),3)
            elif budget_consuntivo == "EFFETTIVO":
                return round (Decimal(self.costoMPEffettivo),3)
            elif budget_consuntivo == "CONSUNTIVO":
                return round (Decimal(self.costoMPConsuntivo), 3)

    def setQuantitaProdotta(self, q, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                self.quantitaBudgetProdotta = q
            elif budget_consuntivo == "STANDARD":
                self.quantitaStandardProdotta = q
            elif budget_consuntivo == "EFFETTIVO":
                self.quantitaEffettivoProdotta = q
            elif budget_consuntivo == "CONSUNTIVO":
                self.quantitaConsuntivoProdotta = q
    
    def getQuantitaProdotta(self, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                return self.quantitaBudgetProdotta
            elif budget_consuntivo == "STANDARD":
                return self.quantitaStandardProdotta
            elif budget_consuntivo == "EFFETTIVO":
                return self.quantitaEffettivoProdotta
            elif budget_consuntivo == "CONSUNTIVO":
                return self.quantitaConsuntivoProdotta

    def setQuantitaVenduta(self, q, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                self.quantitaBudgetVenduta = q
            elif budget_consuntivo == "STANDARD":
                self.quantitaStandardVenduta = q
            elif budget_consuntivo == "EFFETTIVO":
                self.quantitaEffettivoVenduta = q
            elif budget_consuntivo == "CONSUNTIVO":
                self.quantitaConsuntivoVenduta = q
    
    def getQuantitaVenduta(self, budget_consuntivo):
            if budget_consuntivo == "BUDGET":
                return self.quantitaBudgetVenduta
            elif budget_consuntivo == "STANDARD":
                return self.quantitaStandardVenduta
            elif budget_consuntivo == "EFFETTIVO":
                return self.quantitaEffettivoVenduta
            elif budget_consuntivo == "CONSUNTIVO":
                return self.quantitaConsuntivoVenduta

    def setMix(self, m, type):
        if type == "STANDARD":
            self.mixSTD = m
        elif type == "EFFETTIVO":
            self.mixEFF = m

    def getMix(self, type):
        if type == "STANDARD":
            return self.mixSTD 
        elif type == "EFFETTIVO":
            return self.mixEFF

    def setMdc(self, mdc):
        self.mdc = mdc

    def getMdc(self):
        return self.mdc
