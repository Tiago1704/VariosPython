# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 02:50:56 2018

@author: Tiago Ibacache
"""

def particion(ult, ini, fin):
    pos = ini                           

    for i in range(ini, fin):           
        if ult[i] < ult[fin]:             
            ult[i],ult[pos] = ult[pos],ult[i]
            pos += 1

    ult[pos],ult[fin] = ult[fin],ult[pos] 
    return pos

def quick_sort_recursivo(ult, ini, fin):
    if ini < fin:                       
        pos = particion(ult, ini, fin)
        quick_sort_recursivo(ult, ini, pos - 1)
        quick_sort_recursivo(ult, pos + 1, fin)
                                          