import random

cantidadvidas = 0
valido = False #inicio esta variable en false
valido1 = False#Variable para que se ejecute el ciclo, mayor- menor - igual
valido2 = False #Variable para que no se use string a la hora de pedir la cantidad de vidas
numerodejugador = 1#Determina la poscion del jugador
ganada = 0 # Defino para la creacion de un vector, dependiendo de la cantidad de juegadores
perdida = 0 # Defino para la creacion de un vector, dependiendo de la cantidad de juegadores
final = 0 # Activo el clico while, cuando gane un usuario este cambia a distinto de 0

print ("")
print ("MAYOR-MENOR-IGUAL")
print ("")

def vidas(vidas):#Creo una funcion para validar el dato
    try:
        entero = int(vidas)
    except ValueError:
        return False
    return entero
def validar(jugadores):#Creo una funcion para validar el dato
    try: 
        entero = int(jugadores)
    except ValueError:
        return False
    return entero >= 3 and entero <= 5 #Si no esta entre estos valores, devuelve falso

def validar1(datos):#Creo una funcion, para validar el tipeo de los usuario
    try:
     Caracter = str(datos)
    except ValueError:
        return False
    return Caracter=="MAYOR" or Caracter=="MENOR" or Caracter=="IGUAL"

print("Ingrese la cantidad de jugadores, es de 3 a 5 personas .")
while not valido:  #Mientras el valido, sea false realiza el ciclo   
    jugadores=input()
    valido = validar(jugadores) #Utilizo la funcion validar
    if not valido:
     print("El valor ingresado no se encuentra entre 3 y 5. Vuelve a ingresar el valor : ")
    elif jugadores != str():
        ganadas = [0] * int(jugadores) # Defino para la creacion de un vector, dependiendo de la cantidad de juegadores
        perdidas = [0] * int(jugadores) # Defino para la creacion de un vector, dependiendo de la cantidad de juegadores
print("Ingrese la cantidad de puntos de victoria que desean tener")
while not valido2:
    cantidadvidas = input()
    valido2 = vidas(cantidadvidas)
    if not valido2:
        print("El valor ingresado no es un numero, vuelve a ingresarlo")
    if cantidadvidas == str():
        print("El valor ingresado no es un numero, vuelve a ingresarlo")

#Comienzo del juego:

Mazo = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,11,11,11,11,11,12,12,12,12,12,12]#Creacion del mazo
Primernumero = random.choice(Mazo) # Selecciono un valor alatoreo en el vector
Mazo.remove(Primernumero) #Elimino del vector un numero, para jugar con probabilidad 
while final == 0: #Realizar un contador, Cuando gane un usuario, colocar final distinto de 0
    Segundonumero = random.choice(Mazo) #Selecciono un segundo valor del vector, el cual se va a comparar
    Mazo.remove(Segundonumero)
    print("")
    print(f"Turno del jugador {numerodejugador} ")
    print("")
    print(f"El numero para comparar es el : {Primernumero}") 
    print("")
    
    
        
    while not valido1:
            incognita = str(input("Ingresa Mayor , Menor o Igual : "))
            print("")
            incognita = incognita.upper()  
            valido1 = validar1(incognita)#Utiizo la funcion validar1, para comprobar los valores

           
             
    if incognita =="MAYOR":  #Se compara el valor de la incognita 
        if Primernumero < Segundonumero:
            print(f"El numero que salio es el {Segundonumero}")
            print("")
            print(f"Ganaste el numero {Segundonumero} es mayor a {Primernumero}")
            ganadas[numerodejugador-1] = ganadas[numerodejugador-1]+1
                
            
        elif Primernumero == Segundonumero:#Se compara el valor de la incognita 
            print(f"El numero que salio es el {Segundonumero}")
            print("")
            print(f"Perdiste el valor {Primernumero} es igual a {Segundonumero}")
            perdidas[numerodejugador-1] = perdidas[numerodejugador-1] + 1
       
            
        else:#Se compara el valor de la incognita 
            print(f"El numero que salio es el {Segundonumero}")
            print("")
            print(f"Perdiste el numero {Segundonumero} es menor a {Primernumero}")  
            perdidas[numerodejugador-1] = perdidas[numerodejugador-1] + 1
                       
        
    elif incognita == "MENOR":#Se compara el valor de la incognita 
                
            if Primernumero > Segundonumero:#Se compara el valor de la incognita #Se compara el valor de la incognita 
                print(f"El numero que salio es el {Segundonumero}")
                print("")                   
                print(f"Ganaste el numero {Segundonumero} es menor a {Primernumero}")
                ganadas[numerodejugador-1] = ganadas[numerodejugador-1]+1
                    
            elif Primernumero == Segundonumero:#Se compara el valor de la incognita 
                print(f"El numero que salio es el {Segundonumero}")
                print("")
                print(f"Perdiste el valor {Primernumero} es igual a {Segundonumero}")
                perdidas[numerodejugador-1] = perdidas[numerodejugador-1] + 1
                                 
               
            else:#Se compara el valor de la incognita 
                print(f"El numero que salio es el {Segundonumero}")
                print("")
                print(f"Perdiste el numero {Segundonumero} es mayor a {Primernumero}")
                perdidas[numerodejugador-1] = perdidas[numerodejugador-1] + 1
                   
       
    elif incognita == "IGUAL":#Se compara el valor de la incognita 
                
            if Primernumero == Segundonumero:#Se compara el valor de la incognita 
                    print(f"El numero que salio es el {Segundonumero}")
                    print("")
                    ganadas[numerodejugador-1] = ganadas[numerodejugador-1]+1
                    
            elif Primernumero != Segundonumero:#Se compara el valor de la incognita 
                    print(f"El numero que salio es el {Segundonumero}")
                    print("")
                    print(f"Perdiste el valor {Primernumero} es distinto a {Segundonumero}")
                    perdidas[numerodejugador-1] = perdidas[numerodejugador-1] + 1
                     
    
    if len(Mazo)==1: #Se crea para que el mazo cuando el rango del vector sea igual a 1, se modifica el vector
        Mazo = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,11,11,11,11,11,12,12,12,12,12,12]

    print("Las ganadas son") #Va detallando los puntos de victoria de los participantes 
    for i in range(len(ganadas)):               
        print(f"El jugadores {i+1} : > {ganadas[i]} < ")

    print("Las perdidas son") # Se detalla los puntos de derrota de los participantes 
    for i in range(len(perdidas)):               
        print(f"El jugadores {i+1} : > {perdidas[i]} < ")

    for i in range(len(ganadas)):
        if ganadas[i]== int(cantidadvidas): #DEFINO LA CANTIDA DE VICTORIAS POR JUGADOR
            ganador = i
            final = 1
    valido1 = False # RETORNO FALASE PARA QUE PIDA EL VALOR A LOS JUGADORES

    
    Primernumero = Segundonumero # Realizo esto para guarda y volver a comparar los valores
    numerodejugador = numerodejugador+1
    Restarjugador = int(jugadores)+1

    if numerodejugador == Restarjugador:#Realizo esto para voler el contador a 1, y asi poder seguir sumando
        numerodejugador = 1    
print(f"El ganador del juego es el jugador {ganador+1}")
print("Tabla final")
print(ganadas)