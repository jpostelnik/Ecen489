import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from scipy.optimize import minimize

Fs=112e9
M=2**10 
DF=2497
FsDF=Fs/DF
Fin_initial_guess=22e9
print('Fin_initial_guess=',Fin_initial_guess)
FsD=Fs/DF
RID=np.round(Fin_initial_guess/FsD)
FaD=abs(Fin_initial_guess-RID*FsD)
kd=(FsD/2-FaD)*M/FsD
FbinD=M//2-kd
print("Frequency bin decimated=",FbinD)


def func(Fin):
    return DF-abs(Fin-np.round(Fin/FsD)*FsD)/(Fin-np.round(Fin/FsD)*FsD)

Fin_solution=fsolve(func,Fin_initial_guess)
print('Fin_solution=',Fin_solution)
print('expersion is=',func(Fin_solution))
print('at guess=',func(Fin_initial_guess))

Fin=Fin_solution

CDesimated =DF*Fin*M/Fs
R1=np.round(Fin/Fs)
R2=np.round(2*Fin/Fs)
R3=np.round(3*Fin/Fs)

Fa=abs(Fin-R1*Fs)
FaN=Fa/Fs
print('Fa=',Fa)
print('FaN=',FaN)
FH2=abs(Fin-R2*Fs)
FH3=abs(Fin-R3*Fs)

FsD=Fs/DF
R1D=np.round(Fin/FsD)
R2D=np.round(2*Fin/FsD)
R3D=np.round(3*Fin/FsD)
FaD=abs(Fin-R1D*FsD)
print('FaD=',FaD/FsD)
kD=(FsD/2-FaD)*M/FsD
FbinD=M//2-kD
print("frequency bin decimated=",FbinD)
FaD_traget=FsD/2-np.round(kD)*FsD/M
Fin_initial_guess=Fin

def adjust_Fin(Fin):
    return abs(Fin-np.round(Fin/FsD)*Fs)/(Fin-np.round(Fin/FsD)*FsD)

Fin_adjusted=fsolve(adjust_Fin,Fin_initial_guess)

Fin=Fin_adjusted
R1
Fa_adjusted=abs(Fin-R1*Fs)
Fan_adjusted=Fa_adjusted/Fs
print('Fa_adjusted=',Fa_adjusted)

R1D_adjusted=np.round(Fin/FsD)
FaD_adjusted=abs(Fin-R1D_adjusted*FsD)
kD=(FsD/2-FaD_adjusted)*M/FsD
FbindAdjusted=M//2-kD

print("adjusted frequency bin decimated=",FbindAdjusted)

FaD=FaD_adjusted
FaDN=FaD/FsD
FH2D=abs(2*Fin-R2D*FsD)
FH3D=abs(3*Fin-R3D*FsD)