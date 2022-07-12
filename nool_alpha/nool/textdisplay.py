import curses
import time

def test(stdscr, output):
    stdscr.addstr(0, 0, output)

def asc(window, printeditem, ycoord, xcoord):
    splitstring = printeditem.splitlines()
    xminus = splitstring.max
    for y, line in enumerate(printeditem.splitlines(), ycoord):
        window.addstr(y, xcoord - ((len(xminus) // 2)), line)
        window.refresh()
def listp(window, printedlist, ycoord, xcoord):
    for i in printedlist:
        xcoord2 = xcoord - len(printedlist.index(i))//2 
        ycoord2 = ycoord - len(printedlist)//2 + printedlist.index[i]
        window.addstr(ycoord2, xcoord2, row)
        window.refresh()
def pad(pad, text):
    l = 0
    paragraph = text.splitlines()
    for line in paragraph:
        pad.addstr(l, 0)
        l += 1
        pad.refresh()
        
def area(screen, area):
    curses.clear()
    list_print(area)

curses.wrapper(test)
curses.wrapper(asc)
curses.wrapper(listp)
curses.wrapper(pad)
curses.wrapper(area)
