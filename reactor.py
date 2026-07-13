
import math
class CSTR_REACTOR:
    
    def __init__ (self,volume,flowrate,CA0,order):
        self.volume = volume
        self.flowrate = flowrate
        self.CA0 = CA0
        self.order = order
    def conversion (self,k):
        FA0 = self.CA0*self.flowrate

        low = 0.0
        high = 1.0

        for x in range(50):
            X = (low+high)/2
            
            err = FA0*X - (self.volume*k*((self.CA0*(1-X))**self.order))
            
            if (abs(err)<1e-10):
               
                return X
            #direction
            if(err>0):
                high = X
            else:
                low = X
        
        return (low+high)/2
    


    def TFGC (self,conversion,activation_energy,frequency_factor):
        low = 100.0
        high = 2000.0

        for i in range(100):
            mid = (low+high)/2
            err = math.exp(-(activation_energy)/(8.314*mid)) - (self.flowrate*self.CA0*conversion)/(self.volume*frequency_factor*(self.CA0*(1-conversion))**self.order)
            if abs(err) <= 1e-10 :
                return mid
            if err>0:
                high = mid
            else:
                low = mid
        return (low+high)/2
    def VFGC (self,conversion,k):
        if conversion != 1.0:

            req_vol = (self.flowrate*self.CA0*conversion)/(k*(self.CA0*(1-conversion))**self.order)
            return req_vol 
        #else:
         #   req_vol = 10000000000000.00
               
         


    def residencetime(self):
        return self.volume/self.flowrate
    

class PFR_REACTOR:
    def __init__(self,volume,flowrate,concentration,order):
        self.volume  = volume
        self.flowrate=flowrate
        self.concentration = concentration
        self.order = order
    def conversion(self,k):
        CA = self.concentration
        small_volume = 0.01
        segment = int(self.volume/small_volume)
        dv = self.volume/segment
        small_time = dv/self.flowrate

        for x in range(segment):
            
            rate = k*(CA**self.order)
            dCA=small_time*rate
            CA = CA - dCA
        X = (self.concentration - CA)/self.concentration
        
        return X
    def VFGC (self,conversion,k):
        if self.order == 1:
            if conversion != 1:
                a = (self.flowrate*math.log(1/(1-conversion)))/(k)
                return a
        else:
            if conversion != 1:
                a = (self.flowrate*((1-conversion)**(1-self.order)-1))/(k*(self.concentration**(self.order-1))*(self.order-1))
                return a
    def TFGC (self,conversion,frequency_factor,activation_energy):
        if self.order==1:
            temp = math.log((self.flowrate*math.log(1/(1-conversion)))/(self.volume*frequency_factor))
        else:
            temp = math.log((self.flowrate*((1-conversion)**(1-self.order)-1))/(frequency_factor*self.volume*(self.concentration**(self.order-1))*(self.order-1)))
        b = -(activation_energy/8.314)
        return b/temp
