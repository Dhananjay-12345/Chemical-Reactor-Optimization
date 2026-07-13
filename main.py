import matplotlib.pyplot as plt
from reaction import reaction
from reactor import CSTR_REACTOR
from reactor import PFR_REACTOR

frequency_factor=float(input("enter frequency factor : "))
activation_energy=float(input("enter activation energy : "))

#concentration = float(input("enter concentration : "))
order = float(input("enter order : "))
 
volume = float(input("enter volume : "))
flowrate = float(input("enter flowrate  : "))
CA0 = float(input("enter conc : "))



react1 = reaction(frequency_factor,activation_energy)
r1 = CSTR_REACTOR(volume,flowrate,CA0,order)
r2 = PFR_REACTOR(volume,flowrate,CA0,order)
temperature = []
a = int(input("cases : "))
for i in range(a):
    temp=float(input("enter temp : "))
    temperature.append(temp)

tau = r1.residencetime()
Cconversion_list=[]
Pconversion_list=[]

for temp in temperature:
    k = react1.rateconstant(temp)
    X1 = r1.conversion(k)
    X2 = r2.conversion(k)
        
    Cconversion_list.append(X1)
    Pconversion_list.append(X2)
    print(X1 , " " ,X2 , " ")

plt.plot(temperature, Cconversion_list, marker="o", label="CSTR")
plt.plot(temperature, Pconversion_list, marker="s", label="PFR")

plt.xlabel("Temperature (K)")
plt.ylabel("Conversion")
plt.title("CSTR vs PFR Conversion Comparison")

plt.legend()
plt.grid(True)

plt.savefig("CSTR_vs_PFR.png")
plt.show()

#print("_________RESULT__________")
#print("conversion is ", X)
#print("rate constant is ",k)
#print("residence time is ",tau)