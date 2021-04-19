from flask import Flask, render_template
from fabricas import *
from random import choice

app = Flask(__name__)

@app.route('/')
def principal():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()

    otros = fabrica.crear_otros()
    montura = otros.crear_montura()
    personaje = otros.crear_personaje()

    productos = []

    productos.append(arma)
    productos.append(escudo)
    productos.append(montura)
    productos.append(personaje)
    

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)
