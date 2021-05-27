import math


class ModeloMG1:
    def __init__(self, lambdaM, miu, n, desviacion):
        # lambda
        self.media_llegadas = lambdaM
        # miu
        self.media_servicios = miu
        # sigma
        self.desviacion_estandard = desviacion
        # servidores
        self.servidores = 1

        # RO
        self.factor_de_uso = self.media_llegadas / (self.media_servicios)
        self.Pcero = 0
        self.Pn = 0
        self.lq = 0
        self.l = 0
        self.wq = 0
        self.w = 0
        self.n = n

        # Costo
        self.Cn = 0

    def calcularPcero(self):
        self.Pcero = 1 - self.factor_de_uso
        return self.Pcero

    def calcularPn(self):
        if self.n >= 0 and self.n < self.servidores:
            self.Pn = (
                (self.media_llegadas / self.media_servicios) ** self.n
            ) / math.factorial(self.n)
        elif self.n >= self.servidores:
            self.Pn = (
                ((self.media_llegadas / self.media_servicios) ** self.n)
                / (
                    (
                        math.factorial(self.servidores)
                        * (self.servidores ** (self.n - self.servidores))
                    )
                )
                * self.Pcero
            )
        return self.Pn

    # Fórmula de Pollaczek-Khintchine
    def calcularLq(self):
        self.lq = (
            pow(self.media_llegadas, 2) * pow(self.desviacion_estandard, 2)
            + pow(self.factor_de_uso, 2)
        ) / (2 * (1 - self.factor_de_uso))
        return self.lq

    def calcularL(self):
        self.l = self.factor_de_uso + self.lq
        return self.l

    def calcularWq(self):
        self.wq = self.lq / self.media_llegadas
        return self.wq

    def calcularW(self):
        self.w = self.wq + (1 / self.media_servicios)
        return self.w

    def calcularCN(self):
        self.Cn = (self.media_llegadas / self.media_servicios) ** self.n
        return self.Cn


"""
Ejemplo
mg1 = ModeloMG1(3, 5, 1, 0.1)
mg1.calcularPcero()
mg1.calcularPn()
mg1.calcularLq() = 0.5625
mg1.calcularL() = 1.1625
mg1.calcularWq() = 0.1875
mg1.calcularW() = 0.3875
mg1.calcularCN() 
print(mg1.lq)
"""
