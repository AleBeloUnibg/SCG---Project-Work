
class Articolo:
    def __init__(self, codArt):
        self.codArt = codArt

    def setPrezzo(self, p, budget_consuntivo):
            if budget_consuntivo == 0:
                self.prezzoBudget = p
                self.prezzoStandard = p
                self.prezzoEffettivo = p
            elif budget_consuntivo == 3:
                self.prezzoConsuntivo = p
    
    def getPrezzo(self, budget_consuntivo):
            if budget_consuntivo == 0:
                return self.prezzoBudget
            elif budget_consuntivo == 1:
                return self.prezzoStandard
            elif budget_consuntivo == 2:
                return self.prezzoEffettivo
            elif budget_consuntivo == 3:
                return self.prezzoConsuntivo

    def setCosto(self, c, budget_consuntivo):
            if budget_consuntivo == 0:
                self.costoBudget = c
                self.costoStandard = c
                self.costoEffettivo = c
            elif budget_consuntivo == 3:
                self.costoConsuntivo = c
    
    def getCosto(self, budget_consuntivo):
            if budget_consuntivo == 0:
                return self.costoBudget
            elif budget_consuntivo == 1:
                return self.costoStandard
            elif budget_consuntivo == 2:
                return self.costoEffettivo
            elif budget_consuntivo == 3:
                return self.costoConsuntivo

    def setQuantita(self, q, budget_consuntivo):
            if budget_consuntivo == 0:
                self.quantitaBudget = q
            elif budget_consuntivo == 1:
                self.quantitaStandard = q
            elif budget_consuntivo == 2:
                self.quantitaEffettivo = q
            elif budget_consuntivo == 3:
                self.quantitaConsuntivo = q
    
    def getQuantita(self, budget_consuntivo):
            if budget_consuntivo == 0:
                return self.quantitaBudget
            elif budget_consuntivo == 1:
                return self.quantitaStandard
            elif budget_consuntivo == 2:
                return self.quantitaEffettivo
            elif budget_consuntivo == 3:
                return self.quantitaConsuntivo


    def setMix(self, m):
        self.mix = m

    def getMix(self):
        return self.mix

    def setMdc(self, mdc):
        self.mdc = mdc

    def getMdc(self):
        return self.mdc
