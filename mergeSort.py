import time
import random

start = 0
end = 0

def vetorMedio(v,n):
  for x in range(0,n):
    v.append(random.randint(1,n))
  return v

def mergeSort(v,s,e):
	if(s<e):
		m= (s+e)//2
		mergeSort(v,s,m)
		mergeSort(v,m+1,e)
		merge(v,s,m,e)
	return v

def merge(v,s,m,e):
	i=s
	j=m+1
	w=[]
	for k in range(0,e-s+1):
		if (j>e) or ((i<=m) and (v[i]<v[j])):
			w.append(v[i])
			i+=1
		else:
			w.append(v[j])	
			j=j+1
	for i in range(0,e-s+1):
		v[s+i-1]=w[i]
	return v

def tempo():
  for n in range(100,1001,100):
    soma=0
    for j in range(0,1000):
      v=[]
      v=vetorMedio(v,n)
      start = (time.time())
      mergeSort(v,0,n-1)
      end = (time.time())
      soma = soma + end-start
    h=soma/1000
    print(n,h)


tempo()
