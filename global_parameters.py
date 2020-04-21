""" Global parameters file for evaporation simulation """
import numpy as np

""" --------------------------------------- Constants """
eps0 = 8.8541878128E-12
kB = 1.380649E-23
u = 1.66053906660E-27
D2CM = 3.33564E-30

global_parameters = {
    #--------------------------------------- Simulation parameters """
    "tmax": 0.02,  # Time in ms
    "tau": 0.002,  # Time step in ms
    "equilibrationtime": 0.0,
    "writeevery": 0.1,  # Timestep to write the data in ms

    "n": 20,
    
    "bound": 150,
    "collisioncutoff": 0.05,

    # --------------------------------------- Particle parameters
    "m": 127 * u,  # Mass in kg
    "t": 300E-9,  # Initial temperature
    "inelastic": True,  # Set false to turn off inelastic collisions

    # --------------------------------------- Trap parameters
    "depth": 2.5 * 1E-6 * kB,  # Trap depth in J
    "freq": 2 * np.pi * 35,
    
    
    # --------------------------------------- Evaporation parameters
    "a": 0.1 * 0,
    "b": 0.1 * 0,
    "evaporationramp": 20.0
}

meta_data = {"name": '',
             "comment": '',
}

def reactive_cs(vrel):
    # Reactive cross-section based on linear fit to data
    # 0.2D and 23 kHz Trap (ArXiV 1311.0429)
    return 5.763E-5*vrel - 7.05277E-5


def elastic_cs(vrel):
    # Reactive cross-section based on quartic fit to data
    # 0.2D and 23 kHz Trap (ArXiV 1311.0429)
    return -7.525E-6*vrel*vrel*vrel*vrel + 3.095E-4*vrel*vrel*vrel - 4.731E-3*vrel*vrel + 2.913E-2*vrel - 1.469E-3


derived_parameters = {
    'sigtrapinv': 0,
    'fmax': 0,
    'tleninv': 0,
    'emax': 0,
    'sigmaVelocity': 0,
    'sigmaPosition': 0,
    'collisionProbabilityFactor': 0,
    'time': 0,
    'nT': 0,
    'writeEveryInv': 0
}