import math

class reaction:
    def __init__(self,frequency_factor,activation_energy):
        self.A=frequency_factor
        self.Ea=activation_energy
    def rateconstant(self,temperature):
        R = 8.314
        return self.A * math.exp(-(self.Ea)/(R*temperature))
    def ror(self,temperature,concentration,order):
        s=self.rateconstant(temperature)
        return s*(concentration**order)
