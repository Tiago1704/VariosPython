# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 02:10:11 2018

@author: Tiago Ibacache
"""
from threading import Thread,Semaphore
import time, c

class semaforos():
    def __init__(self):
        self.S1 = Semaphore(1)
        self.S2 = Semaphore(1)
        self.S3 = Semaphore(1)
        
def moversemaforos (S1, S2, S3):
    cola = c.Cola()
    c.crearcola(cola)
    
    while (not c.colavacia(cola)):
        S1 = c.insertarcola(cola)
        S2 = c.moveralfinal(cola)
        S3 = c.moveralfinal(cola)
        time.sleep(5)
        S1 = c.moveralfinal(cola)
        S2 = c.insertarcola(cola)
        S3 = c.moveralfinal(cola)
        time.sleep(5)
        S1 = c.moveralfinal(cola)
        S2 = c.moveralfinal(cola)
        S3 = c.insertarcola(cola)
        time.sleep(5)
        
semaforos();
print (moversemaforos(S1, S2, S3));
