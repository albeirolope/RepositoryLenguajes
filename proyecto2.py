import random


alfabetos=[] #Esta es la lista que almacena todos los alfabetos
lenguajes=[] #esta es la lista que almacena los lenguajes

def crearAlfabeto(): #ESta es la funcion que se encarga de crear los alfabetos
    contador=0
    alfabeto=[]
    nCaracteres=int(input("Cuantos caracteres deseas ingresar?: \n"))
    while contador<nCaracteres:
        caracter=str(input("Digite un caracter para el alfabeto: \n"))
        alfabeto.append(caracter)
        contador=contador+1
    alfabetos.append(alfabeto)#Aqui almacenamos la lista alfabeto en la lista principal alfabetos que contiene todos los alfabetos
    print("Gracias por haber creado tu alfabeto \n")

def mostrarAlfabetos():
    print("--------------- Alfabetos ---------------")
    for i in range(len(alfabetos)):
        print(i+1,".",alfabetos[i])
    print("-----------------------------------------")   
def crearLenguaje(alfabeto,n):
    lenguaje=cerraduraDeEstrella(alfabeto,n)
    lenguajes.append(lenguaje)

def mostarLenguaje():
    print("----------------- Lenguajes ----------------")
    for i in range(len(lenguajes)):
        print(i+1, ".",lenguajes[i])
    print("----------------------------------------------")    

def unionAlfabetos(n):
    unido=[]
    c=0
    while c<n:
        indice=int(input("Digite el numero del alfabeto que desea unir: \n"))-1
        unido=unido+alfabetos[indice]
        c=c+1
    return set(unido)
def unionLenguajes(n):
    unido=[]
    c=0
    while c<n:
        indice=int(input("Digite el numero del lenguaje que desea unir: \n"))-1
        unido=unido+lenguajes[indice]
        c=c+1
    return set(unido)
def diferenciaDeConjuntos(n1,n2):
    diferencia=set(n1).difference(n2)
    return diferencia

def interseccionDeConjuntos(n1,n2):
    intersec=set(n1)&set(n2)   
    return intersec

def cerraduraDeEstrella(alfabeto,n):
    palabras=[]
    while len(palabras)<n:
        palabra=''
        for i in range(random.randint(1,len(alfabeto))):
            palabra=palabra+random.choice(alfabeto)
        palabras.append(palabra)
    return palabras

def concatenacionDeLenguajes(l1,l2):
    concatenacionLenguaje=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            concatenacionLenguaje.append(l1[i]+l2[j])

    return concatenacionLenguaje


def potenciaDeUnLenguaje(l1,n): #usamos recursividad para la potencia
    temp=l1
    for i in range(n-1):
        temp=temp+concatenacionDeLenguajes(l1,temp)
        potenciaDeUnLenguaje(temp,n-1)
    return set(temp)

def inversaDeunLenguaje(l):
    lenguaje=l
    for i in range(len(lenguaje)):
        lenguaje[i]=''.join(reversed(lenguaje[i]))
    return lenguaje        


    

#MENU DE OPCIONES
print("¡Hola!, querido usuario, a continuación creara los alfabetos con los cuales realizaré sus requerimientos, recuerde que como minimo debe ingresar 2 alfabetos, GRACIAS. ")
C=0 #creamos un contador
while C<2:
        
    crearAlfabeto()
    C=C+1
    if C>=2:
        OpAl=0
        while OpAl==0:
            OpAl=int(input("¿Deseas ingresar otro alfabeto? Digite 1 para Si, 2 para NO? "))
            if(OpAl==1):
                C=1
            elif(OpAl==2):
                print("Elegiste no crear mas alfabetos")    
            else:
                print("Ingrese una opcion valida")
                OpAl=0    

            
mostrarAlfabetos()


Op=1
while Op != 6: #Se ejecuta mientras op sea diferente de 4
   

    print('1.Realizar Union De Alfabetos\n2.Realizar La Diferencia Entre Lenguajes\n3.Realizar La Interseccion Entre Alfabetos\n4.Calcular La Cerradura De Estrella\n5. Crear lenguajes ---> \n6.Salir ') #Muestra las opciones
    Op = int(input('Ingresa una opcion: ')) # Usuario ingresa opcion
    
    if Op == 1:
        c=True
        while c:
            n=int(input("Digite cuantos alfabetos desea unir : \n"))
            if(n>len(alfabetos)):
                print("No tiene esa cantidad de alfabetos creados, digite una cantidad válida")
            else:
                print( unionAlfabetos(n))
                c=False    
        
    elif Op == 2:
        n1=int(input("Digita el numero del alfabeto que desea hacer la diferecia: \n"))-1
        n2=int(input("Digita el numero del otro alfabeto : \n"))-1
        print(diferenciaDeConjuntos(alfabetos[n1],alfabetos[n2]))
    elif Op == 3:
        n1=int(input("Digita el numero del alfabeto: \n"))-1
        n2=int(input("Digita el numero del otro alfabeto: \n"))-1
        print(interseccionDeConjuntos(alfabetos[n1],alfabetos[n2]))
    elif Op == 4:
        n=int(input("Digite la cantidad maxima de palabras que desea generar con el alfabeto: \n"))
        iAlfabeto=int(input("Digite el numero del alfabeto con el cual desea realizar la cerradura de estrella: \n"))-1
        print(cerraduraDeEstrella(alfabetos[iAlfabeto],n))    
    elif Op == 5:
        i=0
        print("     Hola querido usuario, a continuacion crearas lenguajes aleatorios en base a los alfabetos que creaste anteriormente")
        validacion=True
        while validacion:
            nLenguajes=int(input("      ¿Cuantos lenguajes deseas crear?, recuerda que como minimo deben ser 2 lenguajes: \n"))
            if nLenguajes<2:
                print("     Como minimo debes crear 2 lenguajes")
            else:
                validacion=False
        while i<nLenguajes:
            
            
            n=int(input("       ¿Cuantas palabras desea crear para este lenguaje?: \n"))
            val=True
            while val:
                indiceDeAlfabeto=int(input("        Digite el numero del alfabeto con el que generará el lenguaje: \n"))
                if indiceDeAlfabeto>len(alfabetos):
                    print("     No tiene esa cantidad de alfabetos")
                else:
                    val=False
            crearLenguaje(alfabetos[indiceDeAlfabeto-1],n)
            i=i+1
            
            

            
        print("     ------------- SUB MENU DE LENGUAJES -------------")  
        mostarLenguaje()
        opsubmenu=0
        while opsubmenu!=8:
            print("     1.Calcular union entre lenguajes \n     2.Calcular diferencia entre lenguajes \n     3.Calcular la intersección entre lenguajes\n     4.Calcular la concatenación entre lenguajes\n     5.Calcular la potencia de un lenguaje\n     6.Calcular la inversa de un lenguaje\n     7.Calcular la cardinalidad de un lenguaje \n     8.Salir")  

            opsubmenu=int(input("     Elija una opcion: \n"))

            if opsubmenu==1:
                c=True
                while c:
                    n=int(input("     Digite cuantos lenguajes desea unir : \n"))
                    if(n>len(lenguajes)):
                        print("     No tiene esa cantidad de lenguajes creados, digite una cantidad válida")
                    else:
                        print(unionLenguajes(n))
                        c=False  
            elif opsubmenu==2:
                i1=int(input("     Ingrese el numero del primer lenguaje: \n"))-1
                i2=int(input("     Ingrese el numero del segundo lenguaje: \n"))-1
                print(diferenciaDeConjuntos(lenguajes[i1],lenguajes[i2]))
            elif opsubmenu==3:
                n1=int(input("     Digita el numero del lenguaje:  \n"))-1
                n2=int(input("     Digita el numero del otro lenguaje:  \n"))-1
                print(interseccionDeConjuntos(lenguajes[n1],lenguajes[n2]))
            elif opsubmenu==4:
                n1=int(input("     Digita el numero del lenguaje: \n"))-1
                n2=int(input("     Digita el numero del otro lenguaje: \n"))-1
                print(concatenacionDeLenguajes(lenguajes[n1],lenguajes[n2]))
            elif opsubmenu==5:
                n1=int(input("     Ingrese el numero del lenguaje:  \n "))-1
                n=int(input("     Digite la potencia:  \n"))
                print(potenciaDeUnLenguaje(lenguajes[n1],n))
            elif opsubmenu==6:
                n1=int(input("     Ingrese el numero del lenguaje:  \n "))-1
                print(inversaDeunLenguaje(lenguajes[n1]))
            elif opsubmenu==7:
                n1=int(input("     Ingrese el numero del lenguaje: \n"))-1
                print("     La cardinalidad del lenguaje numero ",n1+1," es: ", len(lenguajes[n1]))
            elif opsubmenu==8:
                pass
    elif Op == 6:
        s= True     
     