#Criado por Ketlly Azevedo de Medeiros 20210051842

import time
import random

start = 0
end = 0

def vetorPior(v,n):
  for i in range(n,0,-1):
    v.append(i)
  return v

def vetorMelhor(v,n):
  for i in range(0,n):
    v.append(i)
  return v

def vetorMedio(v,n):
  for x in range(0,n):
    v.append(random.randint(1,n))
  return v

def insertionSort(v):
  for n in range(1,len(v)):
    k=v[n]
    j=n-1
    while(j>0 and v[j]>k):
      v[j+1]=v[j]
      j=j-1
    v[j+1]=k

def tempoMelhor():
  for n in range(100,1001,100):
    soma=0
    for j in range(0,10000):
      v=[]
      v=vetorMelhor(v,n)
      start = (time.time())
      insertionSort(v)
      end = (time.time())
      soma = soma + end-start
    h=soma/10000
    print(n,h)


def tempoMedio():
  for n in range(100,1001,100):
    soma=0
    for j in range(0,1000):
      v=[]
      v=vetorMedio(v,n)
      start = (time.time())
      insertionSort(v)
      end = (time.time())
      soma = soma + end-start
    h=soma/1000
    print(n,h)

def tempoPior():
  for n in range(100,1001,100):
    soma=0
    for j in range(0,100):
      v=[]
      v=vetorPior(v,n)
      start = (time.time())
      insertionSort(v)
      end = (time.time())
      soma = soma + end-start
    h=soma/100
    print(n,h)

#tempoMelhor() tempoMedio() tempoPior()
tempoMedio()
