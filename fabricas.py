from productos import *
from bridge import *


def funcion_decorador(tipo):
    tipos = ["humanos","orcos"]

    def funcion_interior(clase):
        class Extension(clase):
            if tipo == "humanos":
                def crear_otros(self):
                    return AbstraccionRefinada(FabricaConcretaHumanos()) 
            elif tipo == "orcos":
                def crear_otros(self):
                    return AbstraccionRefinada(FabricaConcretaOrcos()) 
        return Extension
    return funcion_interior

@funcion_decorador(tipo = "humanos")
class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()
    
    def crear_otros(self):
        return AbstraccionRefinada(FabricaConcretaHumanos()) 

@funcion_decorador(tipo = "orcos")
class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

    def crear_otros(self):
        return AbstraccionRefinada(FabricaConcretaOrcos()) 
