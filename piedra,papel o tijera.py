import random     #importo la libreria de aleatorio

contcomputadora=0    #inicio variables en 0
contjugador=0
minusculas= str()
vidas= 0 

print ("")
print ("PIEDRA, PAPEL O TIJERAS")
print ("")

vidas= int(input("Ingrese el numero victorias se debe llegar para ganar: "))  

while vidas == 0:
    print ("El valor ingresado debe ser distinto de 0")
    vidas= int(input("Ingrese el numero victorias se debe llegar para ganar: "))  

print (f"gana el mejor de {vidas} victorias")

while contcomputadora<vidas and contjugador<vidas:    #inicio ciclo mientras
    
    print("")    #salto de linea
    manoComputadora= ["Piedra", "Papel", "Tijera"]   #Genero un vector
    computadora = random.choice (manoComputadora)     #La computadora elige una de las 3 opciones al azar 

    jugador=input("piedra, papel o tijera ")     #Se le pide al jugador que ingrese una de las 3 opciones
    minusculas = jugador.lower()                 #La respuesta del jugador se pasa a minusculas

    if jugador == "piedra" and computadora== "Papel":      #Se comparan las respuestas del jugador y la computadora
        print (f"La computadora eligio: {computadora}")
        print("Papel gana a piedra")
        contcomputadora= contcomputadora +1           #Se le suma 1 al contador del ganador
        print(f"computadora: {contcomputadora}")      #Imprime los contadores 
        print(f"jugador: {contjugador}")

    elif jugador == "piedra" and computadora =="Tijera":
        print (f"La computadora eligio: {computadora}")
        print ("Piedra gana a tijera")
        contjugador = contcomputadora + 1
        print(f"computadora: {contcomputadora}")
        print(f"jugador: {contjugador}")

    elif jugador == "papel" and computadora == "Tijera":
        print (f"La computadora eligio: {computadora}")
        print ("Tijera gana a papel")
        contcomputadora= contcomputadora + 1
        print(f"computadora: {contcomputadora}")
        print(f"jugador: {contjugador}")

    elif jugador == "papel" and computadora == "Piedra":
        print (f"La computadora eligio: {computadora}")
        print ("Papel gana a piedra")
        contjugador = contjugador + 1
        print(f"computadora: {contcomputadora}")
        print(f"jugador: {contjugador}")

    elif jugador == "tijera" and computadora == "Piedra":
        print (f"La computadora eligio: {computadora}")
        print ("Piedra gana a tijera")
        contcomputadora= contcomputadora + 1
        print(f"computadora: {contcomputadora}")
        print(f"jugador: {contjugador}")

    elif jugador == "tijera" and computadora == "Papel":
        print (f"La computadora eligio: {computadora}")
        print ("tijera gana a papel")
        contjugador = contjugador + 1
        print(f"computadora: {contcomputadora}")
        print(f"jugador: {contjugador}")

    elif jugador != "piedra" and jugador != "papel" and jugador != "tijera":  #Cuando el jugador escribe algo que no sean esas 3 opciones imprime el siguiente mensaje
        print("Lo ingresado es incorrecto, debe ingresar piedra, papel o tijera") #Los contadores no se muestran

    else:
        print (f"La computadora eligio: {computadora}")
        print ("Empate")       #Imprime empate cuando las respuestas del jugador y la computadora son iguales
        contjugador = contjugador + 0
        contcomputadora = contcomputadora + 0     #Los contadores no aumentan
        print(f"computadora: {contcomputadora}")
        print(f"jugador: {contjugador}")

if contcomputadora == vidas:                #El primero que llega a 5 es el ganador 
    print ("El ganador es computadora")
else:
    print ("El ganador es el jugador")
