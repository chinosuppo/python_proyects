import random
from diccionario_selecciones_Qatar import selecciones
import string

def seleccion_valida(selecciones):
    seleccion = random.choice(selecciones) # Se elige una selección al azar
    while '-' in seleccion or ' ' in seleccion:
        seleccion = random.choice(selecciones)
    return seleccion.lower()

def ahorcado():
    print('Adivina a las selecciones que participaron del Mundial de Qatar 2022')
    seleccion = seleccion_valida(selecciones)
    letras_seleccion = set(seleccion) # letras en la palabra
    alfabeto = set(string.ascii_lowercase)
    letras_usadas = set() # letras que el usuario ha usado
    vidas = 5
    
    while len(letras_seleccion) > 0 and vidas > 0:
        print('Tienes ', vidas, 'vidas. Tu has usado estas letras: ', ' '.join(letras_usadas)) # letras usadas
        
        lista_de_selecciones = [letra if letra in letras_usadas else '-' for letra in seleccion]
        print('Selección de: ', ' '.join(lista_de_selecciones))
                
        letra_ingresada = input('Ingresa una letra: ').lower() # letras ingresadas por el usuario en el juego
        if letra_ingresada in alfabeto - letras_usadas:
            letras_usadas.add(letra_ingresada)
            if letra_ingresada in letras_seleccion:
                letras_seleccion.remove(letra_ingresada)
                
            else:
                vidas -= 1 # le saco una vida al usuario
                print('La letra no esta en la selección')
    
        elif letra_ingresada in letras_usadas:
            print('Ya ingreso esa letra. Intente con otra!')
        
        else:
            print('Letra incorrecta. Intente de nuevo')
    
    if vidas == 0:
        print('Has perdido :( La selección era: ', seleccion)
    else:
        print('Has adivinado la selección!! Era: ', seleccion)
            

ahorcado()   