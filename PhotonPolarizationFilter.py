import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Fore, Back
init(autoreset=True) #to convert termcolor to wins color

P = 100*np.cos(np.pi/2)**2
print("1. Going through V(ertical) then H(orizontal), the emission is " + Fore.YELLOW + "%.2f%%"%P)

degvh = np.pi/2/2 #45deg
# P = 100*np.cos(degvh)**2**2
P = 100*np.cos(degvh)**2 * np.cos(np.pi/2 - degvh)**2
print("2. Going through V, V-45deg, H, the emission is " + Fore.YELLOW + "%.2f%%"%P)

degvh = np.pi/2 #90deg
P = []
for i in range(13): #0 corresponds to no half-filter between V & H, equivalent to case#1
    P.append(100*np.cos(degvh/(2**i))**(2*2**i))
print("3. Going through V, i number of half-filter, H, the emission is\n" + Fore.YELLOW + "\n".join(['%.5f%%']*len(P))%tuple(P))

degvh = [np.pi/2 * i/100 for i in range(100)] #0-90deg
P = []
for i in degvh:
    P.append(100*np.cos(i)**2 * np.cos(np.pi/2 - i)**2)
print("4. Going through V, V-ideg, H, the emission is " + Fore.YELLOW + "\n".join(['%.5f%%']*len(P))%tuple(P))


