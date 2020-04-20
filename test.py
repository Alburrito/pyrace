import time
import sys
from random import randint



import colorama
colorama.init()
    
def move_cursor(x,y):
    print ("\x1b[{};{}H".format(y+1,x+1))
    
def clear():
    print ("\x1b[2J")
    
clear()
move_cursor(0,0)




size = 30
pistas = []

for i in range(0,3):
    pista = []
    for i in range (0,size):
        pista.append("_")
    pistas.append(pista)

for i in range(0,3):
    time.sleep(1)
    clear()
    move_cursor(0,0)
    randid = randint(0,2)
    pistas[randid][i] = "#"
    for pista in pistas:
        for metre in pista:
            print(metre, end='')
        print("\n")

