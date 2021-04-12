from productos import *

class Fabrica:

    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

    def crear_montura(self):
        pass

    def crear_cuepo(self):
        pass

class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

    def crear_montura(self):
        return MonturaHumano()

    def crear_cuerpo(self):
        return CuerpoHumano()


class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()         

    def crear_montura(self):
        return MonturaOrco()

    def crear_cuerpo(self):
        return CuerpoOrco()