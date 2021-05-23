import math


class ModeloMMS:

    def __init__(self, servidores, lambdaM, miu, n):

        #lambda
        self.media_llegadas = lambdaM
        #miu
        self.media_servicios = miu

        self.servidores = servidores

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
        suma = 0
        for i in range(self.servidores):
            suma += (( self.media_llegadas/ self.media_servicios)** i)/math.factorial(i)
            print(suma)

        self.p0 = 1/(suma + (((( self.media_llegadas/ self.media_servicios)** self.servidores)/math.factorial( self.servidores)) * (1/(1- self.factor_de_uso))))

        return self.p0

    def calcularPn(self):
        if self.n >= 0 and self.n < self.servidores:
            self.Pn = ((self.media_llegadas/self.media_servicios)**self.n)/math.factorial(self.n)
        elif self.n >= self.servidores:
            self.Pn = ((self.media_llegadas/self.media_servicios)**self.n)/((math.factorial(self.servidores)*(self.servidores**(self.n-self.servidores))))*self.p0
        return self.Pn

    def calcularLq(self):

        self.lq =  (self.p0 * pow(( self.media_llegadas/ self.media_servicios), self.servidores) * self.factor_de_uso)/(math.factorial(self.servidores)*pow(1-self.factor_de_uso,2))
        
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