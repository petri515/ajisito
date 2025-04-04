# PRIMER EJERCICIO
""" 
print("Hola, ya se imprimir frases")
 
#   Segundo 

print(420)
 
#   tercero
print(5.3)
 
#1.2.Operaciones básicas y bucles               

# cuarto
suma1,suma2 =1234,532 
print(f"{suma1} + {suma2} = {suma1+suma2} ")

# Quinto
resta1,resta2 =1234,532
print(resta1,"+",resta2,"=", resta1-resta2 )

#   Sexto 

print(1234*532)

#   Septimo

print(1234/532)

#   Octavo
sucesion_1_3 = 0
while sucesion_1_3 < 3:

    sucesion_1_3 += 1

    print(sucesion_1_3)

#   Noveno 
for i in range(1,10):
    print(i)

#   Decimo
numero_1_10k =list(range(1,10001))

print(", ".join(map(str,numero_1_10k)))

#   Undecimo
for i in range(5,11):

    print(i)

#   Duodecimo

for i in range(5,16):

    print(i,end="|",)

#   Decimotercero
sucesion_5_15K = 0
while sucesion_5_15K < 15000:
    sucesion_5_15K += 1
    print(sucesion_5_15K, end=" ")

print("\n")
#   Decimocuarto

holiwis = "hola"

for i in range(200):

    print(holiwis,end=" ")

print("\n")

#   Decimoquinto

for i in range(1,31):
    print(i**2,end=" ")

#   Decimosexto
Y = 1
for i in range(1,21):
     Y = Y*i
print(Y)

#   Decimoseptimo
X = 0
for i in range(1,101):

    X += i**2
print(X)    

#   Decimooctavo
num_in =int(input())
sumilla = 0
for i in range(100):
    sumilla += num_in
    num_in +=1
print(num_in)

#   Decimonoveno    
num_eu = float(input())
num_dola_dola = num_eu * 1.1
print(num_dola_dola)
 
#   Vigesimo

Altura = float(input("Ingrese la altura: "))
anchura = float(input("Ingrese la anchura: "))
print(anchura*Altura)
 
#   Vigesimo primero
num_1 = int(input("numero 1: "))
num_2 = int(input("numero 2: "))

if num_1 > num_2:
    print(num_1, "es el mayor y el menor es ", num_2)
elif num_1 == num_2:
    print("Los numeros son iguales")
else:
    print(num_2, "es el mayor y el menor es", num_1)

#   Vigesimo segundo

nomero = int(input("Numero: "))
numero = nomero
for i in range(nomero):
    if numero%2==1:
        print(numero)
    numero-=1

#   Vigesimotercero

mcd_1 = int(input())
mcd_2 = int(input())

while mcd_1 % mcd_2 !=0 :
	mcd_2 = mcd_1 % mcd_2	

print(mcd_2)

#    Vigesimocuarto
numa = int(input())
numb = int(input())
numc = int(input())

dicr = (numb**2 - 4*numa*numc)**0.5

x1 = (-numb + dicr) / (2*numa)
x2 = (-numb - dicr) / (2*numa)

print(x1,x2)

#    Vigesimoquinto
factorial = int(input("Ingrese el numero para hacer la operacion factorial: "))
resul_fact = factorial
while resul_fact-1 != 0:
    resul_fact-=1 
    factorial= factorial*resul_fact
    
print(factorial)

ackerma_m = int(input("inserte m: "))
ackerma_n = int(input("inserte n: "))

def Ackerman(m,n):
    if m ==0:
        return n+1
    elif m>0 and n==0:
        return Ackerman(m-1,1)
    else:
        return Ackerman(m-1,Ackerman(m,n-1))

print(Ackerman(ackerma_m,ackerma_n))

#   Vigesimosexto

a,b,c = int(input()),int(input()),int(input())

print("El minimo es: ", min(a,b,c))

print("El maximo es: ", max(a,b,c))

#   Vigesimoseptimo
grados_imperia = 0

while grados_imperia < 1000:
    grados_imperia = int(input())
    celcius = 5/9*(grados_imperia-32)
    print(celcius)

#   Vigesimooctavo
for i in range(1,100):
    patata = int(input())
    if patata == 1:
        print("uno")
        
    elif patata == 2:
        print("dos")
        
    elif patata == 3:
        print("tres")
       
    elif patata == 4:
        print("cuatro")
        
    elif patata == 5:
        print("cinco")
"""       
#   Trigesimo
inicio = int(input())
maxi = int(input())

print(f"Números primos entre {inicio} y", maxi, ":")
for num in range(inicio, maxi + 1):
    es_primo = True   
    for i in range(inicio, num):
        if num % i == 0:
            es_primo = False  
            break  

    if es_primo:
        print(num,end=" ")
