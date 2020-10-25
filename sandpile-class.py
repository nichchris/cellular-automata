import numpy as np

class sandpile:
    """ Class for running simulations of the sandpile model by Bak. et al.-1987"""
    def __init__(self, n, thr):
        self.n = n
        self.thr = thr