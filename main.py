#EJERCICIO 1
""" tijera = "tijera"
piedra = "piedra"
papel = "papel"

print("Juego de piedra, papel o tijera. A continuación ingresen sus respuestas en minúsculas...")

jugador1 = input("Jugador 1, ingrese su jugada: ")
jugador2 = input("Jugador 2, ingrese su jugada: ")

if str(jugador1) == tijera and str(jugador2) == papel:
  print("Ganó el jugador 1")
elif str(jugador1) == tijera and str(jugador2) == piedra:
  print("Ganó el jugador 2")
elif str(jugador1) == piedra and str(jugador2) == papel:
  print("Ganó el jugador 2")
elif str(jugador1) == piedra and str(jugador2) == tijera:
  print("Ganó el jugador 1")
elif str(jugador1) == papel and str(jugador2) == piedra:
  print("Ganó el jugador 1")
elif str(jugador1) == papel and str(jugador2) == tijera:
  print("Ganó el jugador 2")
else:
  print("Empataron") """
#Se podría agregar corrección de texto

#EJERCICIO 2
"""i = 0
numeros = list()
while i < 5:
  numero = input("Ingrese un número entero de 1 digito: ")
  numeros.append(numero)
  i = i + 1
print(max(numeros)) """
#Hacer pregunta de por qué cuando son número de muchos digitos, no funciona

#EJERCICIO 3
""" decision = "si"
suma_pares = 0
while decision == "si":
  nums = input("Ingrese un número entero: ")
  if int(nums) % 2 == 0:  
    suma_pares += int(nums)
  decision = input("¿Desea ingresar otro? ")
print(suma_pares) """

#EJERCICIO 4
"""print("Juego para tratar de adivinar un número...")
num = int(input("Jugador 1 ingrese un número entero: "))
intento = int(input("Jugador 2 ingrese su intento: "))
contador = 0 
while int(intento) != int(num):
  if intento < num:
    print("Ese número es muy chico, vuelva a intentarlo con uno más grande")
    intento = int(input("Jugador 2 ingrese su intento: "))
    contador += 1
  elif intento > num:
    print("Ese número es muy grande, vuelva a inentarlo con uno más chico. ")
    intento = int(input("Jugador 2 ingrese su intento: "))
    contador += 1
if intento == num:
  print("¡Felicitaciones, lo adivinates!") 
  print ("Esta es la cantidad de veces que lo intentaste: ",contador)"""

#EJERCICIO 5
"""print("Juego del ahorcado. El primer jugador deberá ingresar una palabra y el segundo adivinarla...\n")

def juego():
  intentos = 6
  palabra_elegida = input("\nJugador 1 ingrese una palabra: ")
  palabra_lista = list(palabra_elegida) 
  guiones = ["_"] * len(palabra_lista)
  print("\nEstos guiones representan la cantidad de letras: ", " ".join(guiones))
  print("\nTenes 6 intentos para averiguar la palabra, buena suerte\n")
  while True:
    letra = input("\nJugador 2 ingrese una letra: ")
    if letra in palabra_lista:
      print("¡Muy bien! adivinaste una letra.")
      for i in range(len(palabra_lista)):
        if palabra_lista[i] == letra:
          guiones[i] = letra
          print(" ".join(guiones))
    else:
      print("Lo siento, esa letra no está en la palabra.")
      intentos -= 1 
      if intentos == 0:
        print("\nPerdiste, no te quedan más intentos, la palabra era:",palabra_elegida)
    print("Intentos restantes:", intentos)
    if guiones == palabra_lista:
      print("\nExacto, la palabra era:",palabra_elegida)
      print("¡Felicitaciones, Adivinaste la palabra!")
      break
      
reiniciar = "si"
while reiniciar == "si":
  juego()
  reiniciar = input("\n¿Desea volver a jugar? ")
print("¡Gracias por usar el programa, adiós!")"""

#EJERCICIO 6
#Hecho la gran parte con ChatGPT, preguntar!!!
#Paso 1: Crear el código secreto y definir varibales necesarias (Contador de intentos, variable código secreto)
#Paso 2: Pedir el ingreso de 4 digitos
#Paso 3: Comprobar intento
#Paso 4: Si los aiertos no son 4, vuelvo a paso 2
#Paso 5: Si acierta que avise que ganó
#Paso 6: Si llega a los 8 intentos que avise que perdió y muestre el código

contador_aciertos = 0
contador_intentos = 8
codigo_lista = []
ingreso_codigo = input("Ingrese el código secreto: ")

for i in ingreso_codigo:
  codigo_lista.append(i)

while contador_intentos != 0:
  adivinar = input("Ingrese el número con el que quiere adivinar el código secreto: ")
  adivinar_lista = []
  contador_aciertos = 0
  for i in adivinar:
    adivinar_lista.append(i)

  contador_intentos -= 1
  
  for i in range(len(codigo_lista)):
    if codigo_lista[i] == adivinar_lista[i]:
      contador_aciertos += 1
    
  print("Adivinaste",contador_aciertos)

  if contador_aciertos == 4:
    print("Ganaste el juego")
    break

  print("Te quedan:", contador_intentos, "intentos")



"""print("Juego 'El Código Oculto' ")
import random
def intentos(intento, codigo):
  contador = 0
  for i in range(4):
    if intento[i] == codigo[i]:
      contador += 1
  return contador

def juego():
  codigo = ''.join(random.sample('1234', 4))
  intentos_restantes = 8
  print("\nIntenta adivinar la cadena de 4 números distintos (del 1 al 4).\n Tienes 8 intentos.")
  while intentos_restantes > 0:
    intento = input("\nIngresa tu adivinanza: ")
    if len(intento) != 4:
      print("Por favor ingresa una cadena de 4 números.")
      continue
        
    intentos_restantes -= 1
    correct_count = intentos(intento, codigo)
    if correct_count == 4:
      print("\n¡GANASTE!")
      return
        
    print(f"Con {intento} has adivinado {correct_count} número(s). Te quedan {intentos_restantes} intentos.")
    
  print(f"Lo siento, la cadena secreta era {codigo}.")

reiniciar = "si"
while reiniciar == "si":
  juego()
  reiniciar = input("\n¿Desea volver a jugar? ")
print("¡Gracias por usar el programa, adiós!")"""





