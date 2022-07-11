import time
import random
###### para rodar o pior caso######
#import sys
#sys.setrecursionlimit(5000)
###################################


start = 0
end = 0

def vetorMedio(v,n):
  for x in range(0,n):
    v.append(random.randint(1,n))
  return v

def vetor(v,n):
  for i in range(0,n):
    v.append(i)
  return v

def quickSort(v,s,e):
	if(s<e):
		p=partition(v,s,e)
		quickSort(v,s,p-1)
		quickSort(v,p+1,e)

def partition(v,s,e):
	#####Descomente para o melhor Caso#####
	#meio=(s+e)//2
	#aux=v[meio]
	#v[meio]=v[e]
	#v[e]=aux
	######################################

	k= v[e]
	i=s-1
	aux=0
	for j in range(s,e):
		if v[j]<= k :
			i+=1
			aux=v[j]
			v[j]=v[i]
			v[i]=aux
	aux=v[e]
	v[e]=v[i+1]
	v[i+1]=aux
	return i+1		

def tempoMelhor():
  for n in range(100,1001,100):
    soma=0
    for j in range(0,10000):
      v=[]
      v=vetor(v,n)
      start = (time.time())
      quickSort(v,0,n-1)
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
      quickSort(v,0,n-1)
      end = (time.time())
      soma = soma + end-start
    h=soma/1000
    print(n,h)

def tempoPior():
  for n in range(100,1001,100):
    soma=0
    for j in range(0,1000):
      v=[]
      v=vetor(v,n)
      start = (time.time())
      quickSort(v,0,n-1)
      end = (time.time())
      soma = soma + end-start
    h=soma/1000
    print(n,h)

tempoPior()