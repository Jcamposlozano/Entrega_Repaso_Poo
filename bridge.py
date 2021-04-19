from productos2 import *

class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

    def crear_montura(self):
        pass

    def crear_personaje(self):
        pass


class Abstraccion():
    def __init__(self, implementador):
        self.__imp__ = implementador

    def crear_montura(self):
        return self.__imp__.crear_montura()
    
    def crear_personaje(self):
        return self.__imp__.crear_personaje()

class AbstraccionRefinada(Abstraccion):

    def operacion_refinada(self):
        return self.__imp__.operacion_implementada_refinada()

class Implementador():
    def operacion_implementada(self):
        pass

class ImplementadorRefinado(Implementador):
    def operacion_implementada_refinada(self):
        pass

class FabricaConcretaHumanos(Fabrica, Implementador):
    def crear_montura(self):
        return MonturaHumano()

    def crear_personaje(self):
        return PersonajeHumano()

class FabricaConcretaOrcos(Fabrica, Implementador):
    def crear_montura(self):
        return MonturaOrcos()

    def crear_personaje(self):
        return PersonajeOrcos()