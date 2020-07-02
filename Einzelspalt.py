import math
def Warscheinlichkeit(a):
    b=0.024001
    L = 6.62*10**-35
    k = math.pi*b*a/L
    return((math.sin(k)/k)**2)

print (Warscheinlichkeit(4.12*10**(-20)))

for n in range(10):
    i=n-5
    a = (i+1)*(10**i)*4.12*10**(-20)
    if a == 0:
        a = 4.12*(10**-30)
    print(a,":",Warscheinlichkeit(a))


