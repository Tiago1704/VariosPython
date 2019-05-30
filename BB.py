# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 01:05:12 2018

@author: Tiago Ibacache
"""

def busquedaBinaria(unaLista, item):
2	    primero = 0
3	    ultimo = len(unaLista)-1
4	    encontrado = False
5	
6	    while primero<=ultimo and not encontrado:
7	        puntoMedio = (primero + ultimo)//2
8	        if unaLista[puntoMedio] == item:
9	            encontrado = True
10	        else:
11	            if item < unaLista[puntoMedio]:
12	                ultimo = puntoMedio-1
13	            else:
14	                primero = puntoMedio+1
15	
16	    return encontrado
17	
18	listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
19	print(busquedaBinaria(listaPrueba, 3))
20	print(busquedaBinaria(listaPrueba, 13))