import math
import numpy as np

class ModeloMMUno:

    def __init__(self, lambdaM, miu, n):
        #lambda
        self.media_llegadas = lambdaM
        #miu
        self.media_servicios = miu

        self.servidores = 1

        self.Cn = 0

        #RO
        self.factor_de_uso = self.media_llegadas/(self.media_servicios*self.servidores)

        
        self.Pcero = 0

        self.Pn = 0
        
        self.lq = 0
        self.l = 0
        
        self.wq = 0
        self.w = 0
        self.n = n
    
    def calcularPcero(self):
  
        self.Pcero = (1/(1-self.factor_de_uso))
     
        self.Pcero = self.Pcero ** -1
        return self.Pcero

    def calcularPn(self):
        print("Para n mayor a " + str(self.n))
        self.Pn = (self.factor_de_uso**self.n)*self.Pcero
        return self.Pn

    def calcularLq(self):
        self.lq =  pow(self.media_llegadas, 2)/ (self.media_servicios * (self.media_servicios - self.media_llegadas))
        return self.lq

    def calcularL(self):
        self.l = self.media_llegadas/ (self.media_servicios - self.media_llegadas)
        return self.l 

    def calcularWq(self):
        self.wq = self.lq / self.media_llegadas 
        return self.wq

    def calcularW(self):
        self.w = self.l/self.media_llegadas 
        return self.w

    def calcularCN(self):
        self.Cn = (self.media_llegadas/self.media_servicios)**self.n
        return self.Cn


