'''
Created on Nov 12, 2016

@author: Alex
'''
import random
from tkinter import *

class Wheel:
    
    def spin(self):
    #returns a random number from the wheel
        num = random.randint(1, 3)
        return num    