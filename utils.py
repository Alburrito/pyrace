import colorama
colorama.init()

def move_cursor(x,y):
    print ("\x1b[{};{}H".format(y+1,x+1))
 
def clear():
    print ("\x1b[2J")
 
def full_clear():
    clear()
    move_cursor(0,0)