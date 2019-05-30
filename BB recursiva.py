# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 02:49:11 2018

@author: Tiago Ibacache
"""

def busquedaBinaria(unaLista, item):
	    if len(unaLista) == 0:
	        return False
	    else:
	        puntoMedio = len(unaLista)//2
	        if unaLista[puntoMedio]==item:
	          return True
	        else:
	          if item<unaLista[puntoMedio]:
	            return busquedaBinaria(unaLista[:puntoMedio],item)
	          else:
	            return busquedaBinaria(unaLista[puntoMedio+1:],item)
	
	listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
	print(busquedaBinaria(listaPrueba, 3))
	print(busquedaBinaria(listaPrueba, 13))