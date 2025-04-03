# PRIMER EJERCICIO

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
for i in range(10):
    print(i)

#   Decimo
"""
numero_1_10k =list(range(1,10001))

print(", ".join(map(str,numero_1_10k)))
"""
#   Undecimo
for i in range(5,11):

    print(i)

#   Duodecimo

for i in range(5,16):

    print(i,end="|",)
    """
#   Decimotercero
sucesion_5_15K = 0
while sucesion_5_15K < 15000:
    sucesion_5_15K += 1
    print(sucesion_5_15K, end=" ")
"""
print("\n")
#   Decimocuarto

holiwis = "hola"

for i in range(200):

    print(holiwis,end=" ")

print("\n")
#   Decimoquinto

for i in range(1,31):
    print(i**2)

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
num_eu = float()
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

#   Vigesimo tercero

