import math


class ModeloMMSK:
    def __init__(self, servidores, lambdaM, miu, n, K):
        # lambda
        self.media_llegadas = lambdaM
        # miu
        self.media_servicios = miu
        self.S = servidores

        self.divLM = lambdaM / miu
        self.Cn = 0
        # RO
        self.factor_de_uso = self.media_llegadas/(self.media_servicios)

        self.Pcero = 0

        self.pn = 0

        self.lq = 0
        self.le = 0
        self.l = 0

        self.wq = 0
        self.w = 0
        self.n = n

        self.K = K

    def P0(self):
        suma = 1.0
        for i in range(1, self.S):
            suma += (pow(self.divLM, i) / math.factorial(i))
        suma += ((pow(self.divLM, self.S) / math.factorial(self.S)) * ((1-pow((self.media_llegadas/(self.S *
                 self.media_servicios)), (self.K-self.S+1))) / (1-(self.media_llegadas/(self.S*self.media_servicios)))))

        self.Pcero = 1/suma
        return self.Pcero

    def Pn(self):
        res = 0
        if self.n < self.S:
            res = ((pow(self.divLM, self.n)) /
                   math.factorial(self.n)) * self.P0()
        else:
            res = ((pow(self.divLM, self.n)) / (math.factorial(self.S)
                                                * pow(self.S, (self.n-self.S)))) * self.P0()
        self.pn = res
        return self.pn

    def Lq(self):
        p = self.media_llegadas / (self.S * self.media_servicios)
        part1 = (self.P0() * pow(self.divLM, self.S) * p) / \
            (math.factorial(self.S) * pow((1 - p), 2))

        part2 = 1 - pow(p, (self.K - self.S)) - \
            ((self.K - self.S) * pow(p, self.K - self.S) * (1 - p))

        self.lq = part1 * part2
        return self.lq

    def Le(self):
        self.le = self.media_llegadas * (1 - self.Pn())
        return self.le

    def Wq(self):
        self.wq = self.Lq() / self.Le()
        return self.wq

    def W(self):
        self.w = self.Wq() + (1/self.media_servicios)
        return self.w

    def L(self):
        le = self.Le()
        w = self.W()
        self.l = le * w
        return self.l
