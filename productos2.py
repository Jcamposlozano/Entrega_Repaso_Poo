from productos import Producto

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class Personaje(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaHumano(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "montura de los humanos"   

class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.png"
        self.descripcion = "montura de los orcos"  

class PersonajeHumano(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/personaje.png"
        self.descripcion = "personaje de los humanos"   

class PersonajeOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/personaje.png"
        self.descripcion = "personaje de los orcos"  