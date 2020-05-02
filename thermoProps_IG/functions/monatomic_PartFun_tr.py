def monatomic_PartFun_tr(m,T,V):
#DESCRIPTION: Computes the translational partition function for a monatomic gas
#AUTHOR: Jay Evans
#DATE: May 1, 2020
#INPUTS:
    # m: Mass of the atom [kg]
    # T: Temperature of the gas [K]
    # V: Volume of the gas [m3]
#OUTPUTS:
    # Z_tr: Translational partition function of the monatomic gas

    import math
    from math import pi

    h = 6.62607004*10**(-34) #Planck's constant [m2-kg/s]
    k_b = 1.38064852*10**(-23) #Boltzmann's constant [m2-kg/s2-K]

    Z_tr = (((2*pi*m*k_b*T)/(h**2.0))**1.5)*V

    return Z_tr
