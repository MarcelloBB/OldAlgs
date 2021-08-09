'''
// PROGRAM NAME:    SUPER PRINT
// AUTHOR      :    MARCELLO BELANDA
// DATE        :    13/06

'''

from random import random
from sys import stdout as s
from time import sleep


def SuperPrint(list_):
    for element in list_:
        s.write(element)
        s.write("\n")
        sleep(0.03)

SuperPrint([str(random()) for i in range(100)])
