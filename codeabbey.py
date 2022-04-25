# -*- coding: utf-8 -*-
"""Codeabbey.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14_3tAYI4Lb_VxtGnYDe4TEwy-RVctFjt

# Sums in Loop
"""

num = int(input())
salida =[]
entry = input().split()
entrada =[int(k) for k in entry]
sum = 0
#a
for j in entrada:   
  sum += j
salida.append(sum)
print(" ".join(map(str, salida)))

"""# Minimum of Two"""

w=int(input())
list_a =[]
list_b =[]
list_c =[]
for i in range(0,w):
  n,m = map(int,input().strip().split(" "))
  list_a.append(n)
  list_b.append(m)

for j in range(len(list_a)):
  a=list_a[j]
  b=list_b[j]
  if a < b: 
    list_c.append(a)
  else:
    list_c.append(b)
 
print(" ".join(map(str, list_c)))

"""# Minimum of Three"""

w=int(input())
list_a =[]
list_b =[]
list_c =[]
list_d =[]
for i in range(0,w):
  n,m,o = map(int,input().strip().split(" "))
  list_a.append(n)
  list_b.append(m)
  list_c.append(o)

for j in range(len(list_a)):
  a=list_a[j]
  b=list_b[j]
  c=list_c[j]
  if a<b:
    if a<c:
      list_d.append(a)
    else: 
      list_d.append(c)
  elif b<c:
    list_d.append(b)
  else:
    list_d.append(c)
 
print(" ".join(map(str, list_d)))

"""# Maximum of array

"""

lista = input().split()
list_a = [int(k) for k in lista]
max = list_a[0]
min = list_a[0]
for i in list_a:
  if max<=i:
    max=i
  if min>=i:
    min=i
print(max, min)

"""# Rounding"""

k = int(input())
respuesta = []
for i in range(0,k):
  n,m = map(int, input().strip().split(" "))
  div_int = n//m; div = n/m; temp= div - div_int
  if temp == 0.5:
    o= int(div + 0.5)
    respuesta.append(o)
  else:
    respuesta.append(round(n/m))
print(" ".join(map(str, respuesta)))

"""# Fahrenheit to Celsius"""

entry = input().split()
list_a = [float(k) for k in entry]
list_a.pop(0)
conv = []
for i in list_a:
    conv.append(round((i-32)/ 1.8))
print(" ".join(map(str, conv)))

"""# Vowel Count"""

vocales=['a','e','i','o','u','y']
w=int(input())
list_a = []
list_b = []
conteo = []
h=0
for i in range(0,w):
  entry = input().replace(" ", "")
  list_a.append(entry)

for k in list_a:
  sum=0
  for j in range(0,6):
    z= vocales[j]
    a_1 = list_a[h].count(z)
    conteo.append(a_1)
  for v in conteo:
    sum=sum+v
  list_b.append(sum)
  
  conteo= []
  h+=1
print(" ".join(map(str, list_b)))

"""# Sum of digits"""

num=int(input())
sigma = []
for i in range(0,num):
  temp = []
  n,m,o = map(int,input().strip().split(" "))
  suma=n*m+o
  sum = 0
  for digit in str(suma):   
    sum += int(digit)
  sigma.append(sum)
print(" ".join(map(str, sigma)))

"""# Arithmetic Progression"""

datos = int(input())
total = []
for i in range(0,datos):
  sum = 0
  a,b,n = map(int,input().strip().split(" "))
  for j in range(0,n):
    P_A=a+j*b
    sum = sum + P_A
  total.append(sum)
print(" ".join(map(str, total)))

"""# Median of Three"""

k = int(input())
mediana = []

for i in range(0, k):
  a,b,c =map(int,input().strip().split(" "))
  
  if a<b:
    if b<c:
      mediana.append(b)
    elif c>a:
      mediana.append(c)
    else:
      mediana.append(a)
  if a>b:
    if b>c:
      mediana.append(b)
    elif c>a:
      mediana.append(a)
    else:
      mediana.append(b)
print(" ".join(map(str, mediana)))

"""# Triangles"""

k= int(input())
show = []

for i in range(0, k):
  lados = []
  l_1,l_2,l_3=map(float, input().strip().split(" "))
  lados.append(l_1); lados.append(l_2); lados.append(l_3); lados.sort()
  temp = lados[0] + lados[1]
  if temp >= lados[2]:
    show.append(1)
  else:
    show.append(0)

print(" ".join(map(str, show)))

"""# Body Mass Index"""

total = int(input())
respuesta = []

for i in range(0, total):
  peso, altura = map(float, input().strip().split(" "))
  bmi = peso/(altura)**2
  
  if bmi < 18.5:
    respuesta.append('under')
  elif 18.5<= bmi <25:
    respuesta.append('normal')
  elif 25<= bmi <30:
    respuesta.append('over')
  else:
    respuesta.append('obese')
    
print(" ".join(map(str, respuesta)))
  #elif

"""#Project Euler

##Problema 1
"""



"""##Problema 2 (4613732)"""

first=0
second=1
sum=0
ac=0
count=1
print("Secuencia de Fibbonacci:")
while(ac < 4000000):
  count+=1
  first=second
  second=sum
  sum=first+second
  if(sum % 2 == 0):
    ac=ac+sum
G=str(sum)
print(G)
len(G)
print(ac)

"""##Problema 3 (6857)"""

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    x=num
    return x

print("introduzca el numero")
numero = int(input()) #aquí se lee el número entero
contador = 0
list=[0]
print("los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        list.append(divisor)
        print(divisor,"es divisor")
        contador += 1
print("el numero ",numero," tiene ",contador," divisores")

print(list)
for i in list:
 print(i,es_primo(i))

"""##Problema 5

Mínimo común multiplo de (1:20)=2.2.2.2.3.3.5.7.11.13.17.19=232792560

##Problema 6 (25164150)
"""

sumacuadrada=0
contadors2=0
totalsc=(5050)**2
vauxiliar=0
print(totalsc)
while contadors2<=100:
  vauxiliar=contadors2**2
  sumacuadrada=sumacuadrada+vauxiliar
  #print(contadors2,":",vauxiliar, "-", sumacuadrada)
  contadors2+=1  
print(sumacuadrada)
print(totalsc-sumacuadrada)

"""##Problema 7 (104743)"""

import math
lista2 = range(104750)
contador=1
for a in lista2:
  cant_divisores = 0
  encontro_divisores = False
  limite=math.sqrt(a)
  i = 2
  while (i <= limite and not encontro_divisores):
      if a % i == 0:
          cant_divisores+=1
          encontro_divisores = True
      i+=1
  if cant_divisores==0 and a>1:
     print(a, " es primo", contador)
     contador=contador+1
print(contador)
print(a)

import math
lista2 = range(19700)
contador=0
x=0
for a in lista2:
  cant_divisores = 0
  encontro_divisores = False
  limite=math.sqrt(a)
  i = 2
  #while (contador <= 49):
  while (i <= limite and not encontro_divisores):
      if a % i == 0:
          cant_divisores+=1
          encontro_divisores = True
      i+=1
  if cant_divisores==0 and a>1:
     contador=0
     #print(a, " es primo", contador)
     
  else:
    contador=contador+1      
    #print(a, " es compuesto", contador)
    if contador == 49:
      x=a
print(x)

"""##Problema 10(142913828922)"""

import math
lista2 = range(2000000)
sum=0
for a in lista2:
  cant_divisores = 0
  encontro_divisores = False
  limite=math.sqrt(a)
  i = 2
  while (i <= limite and not encontro_divisores):
      if a % i == 0:
          cant_divisores+=1
          encontro_divisores = True
      i+=1
  if cant_divisores==0 and a>1:
     # print(a, " es primo")
     sum=sum+a
print(sum)

"""##Problema 20 (648)"""

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 100

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

num = factorial
  
print ("The original number is " + str(num)) 
  
res = [int(x) for x in str(num)] 
  
print ("The list from number is " + str(res))

contador=0
suma=0
for i in res:
  x=res[contador]
  contador=contador+1
  #print(x)
  suma=x+suma
  #print(suma)
print(suma)

"""##Problema 25 (4781)"""

n=int(input("ingrese un n:"))
first=0
second=1
sum=0
count=0
print("secuencia de Fibonacci")
while(count<=n):
  count+=1
  first=second
  second=sum
  sum=first+second
G=str(sum)
print(G)
len(G)