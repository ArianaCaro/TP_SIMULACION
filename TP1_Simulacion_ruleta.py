import random
import pandas as pd
import matplotlib.pyplot as plt

def generar_ruleta(corrida, tiradas):
    nros_ruleta = []
    for i in range(corrida):
        for j in range(tiradas):
            nro_ganador = random.randint(0,36)
            nros_ruleta.append(nro_ganador)
    return nros_ruleta

def grafica(rtados):
    plt.xlabel('tiradas')
    plt.ylabel('')
    plt.show()


    """
    Inicio del programa
    """
def inicio():
    tiradas= int(print("Ingrese la cant de tiradas: "))
    corridas= int(print("Ingrese la cant de corridas: "))
    nro = int(print("Ingrese un nro entre 1 y 36: "))
    if 1 <= nro <= 36:
        rtados = generar_ruleta(corridas, tiradas)
        #graficar(rtados)