import math 
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
from neuron import Neuron

def s_t(t):
    if 10 <= t <= 11 or 20 <= t <= 21 or \
            30 <= t <= 40 or 50 <= t <= 51 or \
            53 <= t <= 54 or 56 <= t <= 57 or \
            59 <= t <= 60 or 62 <= t <= 63 or \
            65 <= t <= 66:
        return 150
    return 0

def stimulus(t):
        if t > 10 and t < 11:
            return 150
        elif t > 20 and t < 21:
            return 150
        elif t > 30 and t < 40:
            return 150
        elif t > 50 and t < 51:
            return 150
        elif t > 53 and t < 54:
            return 150
        elif t > 56 and t < 57:
            return 150
        elif t > 59 and t < 60:
            return 150
        elif t > 62 and t < 63:
            return 150
        elif t > 65 and t < 66:
            return 150
        return 0
neuron = Neuron(stimulus)
neuron.plot_activity()