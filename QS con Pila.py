# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 02:05:17 2018

@author: Tiago Ibacache
"""

import P

def quicksortConLista (pila, izq, der):
    pila = P.Pila()
    P.crearpila(pila)
    i = izq
    d = der
    med = pila[(izq + der)/2]
    
    while (i <= d):
        while pila[i] < med and d <= der:
            i = i + 1
        while med < pila[i] and d >= izq:
            d = d - 1
            if i<=d:
            aux = pila[i]; pila[i] = pila[d]; pila[d] = aux;
            i = i + 1;  d = d - 1;
            
        if izq < d:
            quicksort(pila, izq, d)
    if i < der:
        quicksort(pila, i, der)
def imprimirQS (P, tam):
    P.mostrar_pila(pila)
    
def leePila():
    pila = []
    cantN = int (raw_input("Cantidad de numeros a ingresar: "))
    
    for i in range (0, cantN):
        pila.append(int(raw_input("Ingrese el numero %d: ") % i))
        return pila
    
A = leepila()
quicksort(A, 0, len(A)-1)
imprimeQS(A, len(A))        