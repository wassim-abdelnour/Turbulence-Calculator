#!/usr/bin/env python

"""Calculator of Initial Values and Boundary Conditions of K-e and k-w Turbulence Models"""

__author__ = "Wassim Abdel Nour"
__version__ = "1.0"


import math

#input Surface Area and Perimeter of Inlet
print('Entre :\n')
mass_flow_rate = float( input('\tMass Flow Rate : '))
rho = float( input('\tFluid Density : '))
mu = float( input('\tFluid Dynamic Viscosity : '))
S = float( input('\tInlet Surface Area : '))
P = float( input('\tInlet Perimeter : '))
print('\n')

#Hydraulic Diameter = 4*Surface_Area/Perimeter
Hd = 4*S / P

#mass_flow_rate = rho * V * S
Vmean = mass_flow_rate / (rho*S)

#free-stream velocity
Vinf = 2*Vmean #ideal for round inlets

#Calculation of Reynold's Number
Re = rho * Vmean * Hd / mu

#Calculation of I (Turbulence Intensity)
I = 0.16*pow(Re, -1/8)

#Calculation of kappa (Turbulent kinetic Energy)
k = 1.5 * Vinf*Vinf * I*I

#Calculaction of mixing length or turbulent length scale
l = 0.07 * Hd #mixing length or turbulent length scale

#Calculaction of epsilon (turbulent dissipation rate)
eps = (math.pow(0.09,0.75)*math.pow(k,1.5)) / (l)

#Calculaction of nut (turbulent viscosity)
nut = 0.09 * k*k/eps

#Calculaction of omega (specific turbulent dissipation rate)
omega = math.pow(0.09, -0.25) * math.sqrt(k)/l

print('Reynold\'s Number Re = ', Re)
print('Turbulent Kinetic energy k = ', k)
print('Turbulent Dissipation Rate eps = ', eps)
print('Turbulent Viscosity nut = ', nut)
print('Specific Turbulent Dissipation Rate omega = ', omega)
