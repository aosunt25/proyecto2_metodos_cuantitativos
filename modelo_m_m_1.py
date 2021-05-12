class ModeloMMUno:

    def _init_(self):

        self.media_llegadas = 0
        self.media_servicios = 0
        self.factor_de_uso = self.media_llegadas/(self.media_servicios * self.clientes)
        self.clientes = 0
        
        self.lq = 0
        self.l = 0
        
        self.wq = 0
        self.w = 0

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