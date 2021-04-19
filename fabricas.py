from productos import *
from bridge import *

class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()
    
    def crear_otros(self):
        return AbstraccionRefinada(FabricaConcretaHumanos()) 


class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

    def crear_otros(self):
        return AbstraccionRefinada(FabricaConcretaOrcos()) 
