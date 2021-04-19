from productos import *
from bridge import *

def funcion_decorador(tipo):
    tipos = ["1","2"]

    def funcion_interior(clase):
        class Extension(clase):
            if tipo == "1":
                def crear_otros(self):
                    return AbstraccionRefinada(FabricaConcretaHumanos()) 
            elif tipo == "2":
                def crear_otros(self):
                    return AbstraccionRefinada(FabricaConcretaOrcos()) 
        return Extension
    return funcion_interior

@funcion_decorador(tipo = "1")
class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

@funcion_decorador(tipo = "2")
class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()


