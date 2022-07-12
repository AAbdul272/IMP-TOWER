import curses
from curses import wrapper
import random
import time

# The maximum value for y and x in stdscr are 25 and 80 respectively, the window is in the (+, -) quadrant

menuSelect = ["1 - NEW GAME", "2 - CONTINUE", "3 - CREDITS", "4 - EXIT"]

def test_print(stdscr, output):
    stdscr.addstr(0, 0, output)

def asc_print(window, printeditem, ycoord, xcoord):
    splitstring = printeditem.splitlines()
    xminus = splitstring.max
    for y, line in enumerate(printeditem.splitlines(), ycoord):
        window.addstr(y, xcoord - ((len(xminus) // 2)), line)
        window.refresh()
def list_print(window, printedlist, ycoord, xcoord):
    for i in printedlist:
        xcoord2 = xcoord - len(i)//2 
        ycoord2 = ycoord + printedlist.index(i)
        window.addstr(ycoord2, xcoord2, i)
        window.refresh()
def pad_print(pad, text):
    l = 0
    paragraph = text.splitlines()
    for line in paragraph:
        pad.addstr(l, 0)
        l += 1
        pad.refresh()
        
def area_print(screen, area):
    curses.clear()
    list_print(area)


def choose_function(input_number, choice_dict):
    for c in choice_dict:
        if input_number == c:
            choice_dict[c]()

def new_game():
    stdscr.erase()
    stdscr.addstr(13, 38, 'testing')

def load_game():
    pass

def about_game():
    pass

def exit_game():
    curses.exit()

startmenu_dict = {1: new_game, 2: load_game, 3: about_game, 4: exit_game}

def start_screen(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    
    h, w = stdscr.getmaxyx()
    centralx = w // 2
    centraly = h // 2
    openingcredits = "---AABDUL272 PRESENTS---"
    gamename = """
----------------------------------------------------
| xxxxx  x x  xxxx    xxxxx xxxxx x x x xxxxx xxxxx  |
|   x   x x x x   x     x   x   x x x x x     x  xx  |
|   x   x x x xxxx      x   x   x x x x xxxxx xxx    |
|   x   x x x x         x   x   x x x x x     x x    |
| xxxxx x x x x         x   xxxxx  x x  xxxxx x  xx  |
----------------------------------------------------
"""
    gamename1 = "x   x  xxx  x   x  x     xxxxx   xxxxx xxxxx   xx  x xxxxx xxxxx x"
    gamename2 = "x   x x   x x   x  x       x     x   x x       x x x x   x x   x x"
    gamename3 = " x x  xxxxx x   x  x       x     x   x xxxxx   x  xx x   x x   x x"     
    gamename4 = "  x   x   x  xxx   xxxxx   x     xxxxx x       x   x xxxxx xxxxx xxxxx"     
    stdscr.addstr(centraly, centralx - (len(openingcredits) // 2), openingcredits)
    stdscr.refresh()
    time.sleep(2)
    stdscr.erase()
    for y, line in enumerate(gamename.splitlines(), centraly - 10):
        stdscr.addstr(y, centralx - ((len(line) // 2)), line)
    # stdscr.addstr(centraly - 3, 40, gamename)    
    # stdscr.addstr(centraly - 12, centralx - (len(gamename1) // 2), gamename1)
    # stdscr.addstr(centraly - 14, centralx - (len(gamename2) // 2), gamename2)
    # stdscr.addstr(centraly - 16, centralx - (len(gamename3) // 2), gamename3)
    # stdscr.addstr(centraly - 18, centralx - (len(gamename4) // 2), gamename4)
    stdscr.refresh()
    time.sleep(1)
    stdscr.addstr(centraly + 2, centralx - len("-Press 0 to continue-")//2, "-Press 0 to continue-")
    menu = False
    stdscr.refresh()
    while menu == False:
        proceed = str(stdscr.getch())
        test_print(stdscr, proceed)
        time.sleep(0.5)
        if proceed[0:2] == '48':
            stdscr.erase()
            for y, line in enumerate(gamename.splitlines(), centraly - 10):
                stdscr.addstr(y, centralx - ((len(line) // 2)), line)
            stdscr.refresh()
            list_print(stdscr, menuSelect, 13, centralx)
            menu = True
            stdscr.refresh()
            time.sleep(3)
        else:
            menu = False
            stdscr.refresh()
    stdscr.refresh()
    menu2 = False
    while menu2 == False:
        proceed2 = stdscr.getkey()
        test_print(stdscr, proceed)
        choose_function(proceed, startmenu_dict)



                                                           
