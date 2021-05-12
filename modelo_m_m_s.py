import math


class ModeloMMS:

    def _init_(self):

        self.media_llegadas = 0
        self.media_servicios = 0
        self.factor_de_uso = self.media_llegadas/(self.media_servicios * self.clientes)
        self.clientes = 0
        
        self.p0 = 0

        self.lq = 0
        self.l = 0
        
        self.wq = 0
        self.w = 0

    def calcularP0(self):
        suma = 0
        for i in range(0, self.clientes - 1):
            suma += pow(( self.media_llegadas/ self.media_servicios), i)/math.factorial(i)

        self.p0 = suma + pow(( self.media_llegadas/ self.media_servicios), self.clientes)/math.factorial( self.clientes) * (1/(1- self.factor_de_uso))

        return self.p0

    def calcularLq(self):

        self.lq =  (self.p0 * pow(( self.media_llegadas/ self.media_servicios), self.clientes) * self.factor_de_uso)/(math.factorial(self.clientes)*pow(1-self.factor_de_uso,2))
        
        return self.lq

    def calcularL(self):
        self.l = self.lq + self.media_llegadas/self.media_servicios
        return self.l 

    def calcularWq(self):
        self.wq = self.lq / self.media_llegadas 
        return self.wq

    def calcularW(self):
        self.w = self.wq + 1/self.media_servicios 
        return self.w