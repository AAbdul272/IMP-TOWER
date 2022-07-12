import curses
import random
import time
import nool

current_location = []
current_area = 

def FUCK_YOU(stdscr):
    stdscr.addstr(10, 10, str(stdscr.getmaxyx()))
    stdscr.refresh()
    time.sleep(15)
    stdscr.refresh()
    
curses.wrapper(FUCK_YOU)

def commence_turn(turn_order, party, enemy_party, inventory):
    next_move = []
    for unit in turn_order:
        next_move.append(turn_order[x])
    next_move.sort()
    luckyguy = turn_order[next_move[0]]
    luckyguy.choice(party, enemy_party, inventory)
    
def enemy_encounter(party, enemy_party, inventory):
    victory = False
    defeat = False
    all_parties = party + enemy_party
    turn_order = {}
    for unit in all_parties:
        delay = unit.speed
        turn_order.update({unit: delay})
    while (victory and defeat) == False:
        status.genstatus_check(party, enemy_party, victory, defeat)
        commence_turn(turn_order, party, enemy_party, inventory)
    elif victory == True
    victory_screen(party, enemy_party, inventory, dungeon)
    elif defeat == True
    game_over()
class Area(object):
    def __init__(self, location, entrance, exit_room):
        self.location = location
        self.entrance = entrance
        self.exit = exit_room
    def enter(self, character):
        pass
    def exit(self, character):
        pass

class DungeonGrid(Area):
    def __init__(self, grid, first_entrance):
        self.grid = grid
        self.first_entrance = first_entrance
    def move(self):
        grid_location = current_location
        current_x = current_location[0]
        current_y = current_location[1]
        north = "North - " + self.enter[current_x][current_y + 1][0]
        south = "East - " + self.enter[current_x][current_y - 1][0]
        east = "South - " + self.enter[current_x + 1][current_y][0]
        west = "West - " + self.enter[current_x - 1][current_y][0]
        compassloc_display = '''
{}

{}

{}

{}
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

Press 1 to go North, 2 to go East, 3 to go South and 4 to go West
        '''.format(north, east, south, west)
        here = True
        while here == True:
            direction = stdscr.getkey()
            if direction == 1:
                if [current_x][current_y + 1][1] == blank:
                    here = True
                else:
                    here = False
                    self.enter([current_x], [current_y + 1])
            elif direction == 2:
                if [current_x + 1][current_y][1] == blank:
                    here = True
                else:
                    here = False
                    self.enter([current_x + 1], [current_y])
            elif direction == 3:
                if [current_x][current_y - 1][1] == blank:
                    here = True
                else:
                    here = False
                    self.enter([current_x], [current_y - 1])
            elif direction == 4:
                if [current_x - 1][current_y][1] == blank:
                    here = True
                else:
                    here = False
                    self.enter([current_x - 1], [current_y])
            elif (direction in range(1, 5)) == False:
                here == True
    def enter(self, x_coord, y_coord):
        current_location = [x_coord, y_coord]
        self.grid[x_coord][y_coord][1]()
    def chest(self, inventory, current_gold, drops):
        for item in drops:
            if item[len(item) - 1] == 'g':
                current_gold += int(item[1:])
            else:
                inventory.append(item)
        self.move()
    def npc_encounter(self, text, function):
        textadv_print(text)
        function()
    def scripted_encounter(self, text, function):
        pass

class Town(Area):
    
