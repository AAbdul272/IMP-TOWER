import math
import random
from random import randint
from math import *

expTest = 100




# Basic functions for combat interactions

def impede(target):
        if target.casting == True:
                target.casting = False
                target.spell = []
                target.spelltarget = []
                
def buff(serum, character):
        if serum.effect[5:] > 5:
            character.resist[serum.effect[5:]] += serum.effectValue / serum.effectValue2
        else:
            character.attribute[serum.effect[5:]] += serum.effectValue / serum.effectValue2

def recover(bar, maxbar, value):
    bar += value
    if bar > maxbar:
        newvalue = value + maxbar - bar
        bar = maxbar
        return newvalue
    
def damage(target, value):
    schmuck.hp -= value
    return("{} recieves {} damage!".format(schmuck.name, value))
    if schmuck.hp <= 0 and schmuck.character == True:
        return("{} is slain...".format(schmuck.name))
        schmuck.alive == False
        schmuck.hp == 0
    elif schmuck.hp <= 0:
        return("Vanquished {}!".format(schmuck.name))
        schmuck.alive == False
        schmuck.hp == 0

def tick_damage(target, value):
    schmuck.hp -= value
    if schmuck.hp <= 0 and schmuck.character == True:
        return("{} is slain...".format(schmuck.name))
        schmuck.alive == False
        schmuck.hp == 0
    elif schmuck.hp <= 0:
        return("Vanquished {}!".format(schmuck.name))
        schmuck.alive == False
        schmuck.hp == 0

def hit(target):
        pass





# Collection of all the item class definitions

class Item(object):
    def __init__(self, name, maxQuantity):
        self.name = name
        self.quant = maxQuantity
    def acquire(self, inventory, amount):
        if self.name in inventory == True: 
                for x in range(0, amount + 1):
                    inventory[self.name] += 1
        else:
                inventory.update({self.name: 0})
                for x in range(0, amount + 1):
                    inventory[self.name] += 1
    def remove(self, inventory, amount):
        for x in range(0, amount + 1):
                inventory[self.name] -= 1
        if inventory[self.name] <= 0:
                inventory.remove({self.name})
                
class Usable(Item):
    def __init__(self, name, maxQuantity, effect, effectValue, effectValue2):
        self.name = name
        self.quant = maxQuantity
        self.effect = effect
        self.effectValue = effectValue
        self.effectValue2 = effectValue2
    def use_item(self, character, inventory):
        self.effect(self, character)
        remove(self, inventory, amount)
                                
class Key(Item):
    pass

class Magic(Item):
    def __init__(self, name, spell, mpCost, stats, compClass):
            self.name = name
            self.spell = spell
            self.mpCost = mpCost
            self.stats = stats
            self.compClass = compClass
    def cast_spell(self, caster, target):
            caster.mp -= self.cost
            self.spell(caster, target)

class Gear(Item):
    def __init__(self, name, maxQuantity, stats, category):
        self.name = name
        self.quant = maxQuantity
        self.stats = stats
        self.category = category
    def equip(self, character, party_inventory):
        if character.equips[self.category] == "Empty" and self.name in party_inventory:
            party_inventory[self.name] -= 1
            character.equips[self.category] = self
    def unequip(self, character, category, party_inventory):
        party_inventory[self.name] += 1
        character.equips[category] = "Empty"

class Armor(Gear):
    def __init__(self, name, maxQuantity, stats, category):
        self.name = name
        self.quant = maxQuantity
        self.stats = stats
        self.category = category

class Trinket(Gear):
    def __init__(self, name, maxQuantity, stats, category, enchant, disenchant):
        self.name = name
        self.quant = maxQuantity
        self.stats = stats
        self.category = category
        self.enchant = enchant
        self.disenchant = disenchant
    def equip(self, character, party_inventory):
        if character.equips["Trinket1"] == "Empty" and self.name in party_inventory:
            party_inventory[self.name] -= 1
            character.equips[self.category] = self
            self.enchant(character)
        elif character.equips["Trinket2"] == "Empty" and self.name in party_inventory:
            party_inventory[self.name] -= 1
            character.equips[self.category] = self
            self.enchant(character)
        else:
                pass
    def unequip(self, character, category, party_inventory):
        party_inventory[self.name] += 1
        character.equips[self.category] = "Empty"
        self.disenchant(character)
        
class Weapon(Gear):
    def __init__(self, name, maxQuantity, stats, category):
        self.upgrade = 0
        self.name = name + '+{}'.format(self.upgrade)
        self.quant = maxQuantity
        self.stats = stats
        self.category = category
        

# self.stats = ceil(stats * 2**(math.log(party_inventory)))

weaponstats_template = {"bluntAttack": 9, "pierceAttack": 9, "slashAttack": 9, "darkAttack": 9, "fireAttack": 9, "iceAttack": 9, "boltAttack": 9, "AttackSpeed": 1}

import items
from items import *

# Party related status data

party_inventory = {}





# Race related data

resist_tuple = ("darkResist", "fireResist", "iceResist", "boltResist", "bluntDef", "pierceDef", "slashDef", "magicDef", "poisonDef")

Elf = {"darkResist": -0.2, "fireResist": -0.2, "iceResist": 0.0, "boltResist": 0.1, "bluntDef": 0.0, "pierceDef": 0.1, "slashDef": 0.2, "magicDef": 0.2, "poisonDef": 0.2}
Kobold = {"darkResist": 0.1, "fireResist": 0.2, "iceResist": 0.0, "boltResist": 0.0, "bluntDef": 0.2, "pierceDef": 0.0, "slashDef": -0.2, "magicDef": 0.1, "poisonDef": -0.2}
Minotaur = {"darkResist": -0.1, "fireResist": -0.3, "iceResist": 0.2, "boltResist": -0.2, "bluntDef": 0.3, "pierceDef": 0.3, "slashDef": 0.3, "magicDef": -0.2, "poisonDef": 0.1}
Human = {"darkResist": 0.2, "fireResist": 0.1, "iceResist": 0.1, "boltResist": 0.2, "bluntDef": -0.2, "pierceDef": -0.2, "slashDef": 0.1, "magicDef": 0.0, "poisonDef": 0.0}

race_dict = {"E": Elf, "K": Kobold, "T": Minotaur, "H": Human}

{"HP": 1.0, "MP": 1.0, "STR": 1.0, "DEX": 1.0, "INT": 1.0, "EVA": 1.0, "ACC": 1.0}

master_class_dict = {
        "Mage": {"HP": 0.5, "MP": 1.6, "STR": 0.5, "DEX": 1.0, "INT": 2.5, "EVA": 1.1, "ACC": 0.8, "SPD": 1.1},
        "Summoner": {"HP": 0.9, "MP": 1.4, "STR": 0.8, "DEX": 1.0, "INT": 1.5, "EVA": 1.3, "ACC": 1.0, "SPD":  0.9}, 
        "Rogue": {"HP": 0.7, "MP": 0.6, "STR": 0.6, "DEX": 2.1, "INT": 1.7, "EVA": 1.7, "ACC": 1.8, "SPD": 1.5},
        "Dragoon": {"HP": 1.2, "MP": 0.4, "STR": 1.5, "DEX": 1.7, "INT": 1.2, "EVA": 2.3, "ACC": 1.5, "SPD": 1.3},
        "Knight": {"HP": 1.5, "MP": 0.8, "STR": 1.9, "DEX": 1.0, "INT": 1.1, "EVA": 1.2, "ACC": 1.2, "SPD": 0.8},
        }


# Character related data

class Plunger(object):
    def __init__(self, name, level, job, race):
        self.name = name
        self.level = level
        self.job = job
        self.race = race
        self.maxhp = ceil((20 + 10*(self.level))*master_class_dict[self.job["Class"]]["HP"])
        self.maxmp = ceil((9 + 7*(self.level))*master_class_dict[self.job["Class"]]["MP"])
        self.str = ceil((3 + 2*(self.level))*master_class_dict[self.job["Class"]]["STR"])
        self.dex = ceil((3 + 2*(self.level))*master_class_dict[self.job["Class"]]["DEX"])
        self.int = ceil((3 + 2*(self.level))*master_class_dict[self.job["Class"]]["INT"])
        self.acc = ceil(50 * master_class_dict[self.job["Class"]]["ACC"])
        self.speed = ceil(50 * master_class_dict[self.job["Class"]]["SPD"])
        self.hp = self.maxhp
        self.mp = self.maxmp
        self.undeath = 0
        self.currentExp = 0
        self.equips = {"Helm": issued_cap, "Armor": issued_outfit, "Gloves": issued_gloves, "Weapon": self.job(0), "Sidearm": "Empty", "Trinket1": "Empty", "Trinket2": "Empty"}
        # add ', job, race, equips' later
        # self.equips = dict(gear)
        self.active = True
        self.alive = True
        self.totalExp = (self.level)**2
        self.absorb = race_dict[self.race]
        self.casting = False
        self.character = True 
        self.spell = []
        self.spelltarget = []
        self.skills = []
        self.target = True
        for x in resist_tuple:
            self.resist.append(race_dict[self.race][x])
        self.immune = []
        for x in range (1,7):
            self.immune.append(False)
        self.inflict = {"poison": False, "petrify": False, "paralyse": False, "blind": False, "burn": False, "frostbite": False, "death": False, "curse": False, "wither": False, "spellbind": False}
        self.tick = {}
        for x in negstatus_list:
                self.tick.update({x: 0})
    def exp_gain(self, expGained):
        self.currentExp += int(expGained)
        if self.level < 60:
            if (self.alive and self.active) == True and self.currentExp >= self.totalExp:
                self.currentExp = self.currentExp - self.totalExp
                self.level += 1
                return ("{} GAINS {} EXP!".format(self.name, expGained))
                return ("{} LEVELS UP TO LV {}!".format(self.name, self.level))
                self.totalExp = (self.level)**2
                self.maxhp = ceil((20 + 10(self.level))*master_class_dict[self.job[0]]["HP"])
                self.maxmp = ceil((9 + 7(self.level))*master_class_dict[self.job[0]]["MP"])
                self.str = ceil((3 + 2(self.level))*master_class_dict[self.job[0]]["STR"])
                self.dex = ceil((3 + 2(self.level))*master_class_dict[self.job[0]]["DEX"])
                self.int = ceil((3 + 2(self.level))*master_class_dict[self.job[0]]["INT"])
            elif (self.alive and self.active) == True:
                return ("{} GAINS {} EXP!".format(self.name, int(expGained)))
            else:
                self.currentExp = self.currentExp - expGained
    def choice(self, party, enemy_party): 
        if self.casting == True:
                spell = self.spell
                spell.cast(self.spelltarget)
                self.spell = []
                self.spelltarget = []
                self.casting = False
        elif self.casting == False:
                pass
    def placeholder(self):
        pass

# for i in range(1, 100):
    # testchar.exp_gain(testchar.totalExp)





# Monster class definition

class Monster(object):
    def __init__(self, name, level, drop, race):
            self.name = name
            self.level = level
            self.drop = drop
            exp_drop = 0
            self.race = race
            self.absorbs = race_dict[self.race]
            self.character = False
            self.active = True
            self.alive = True
            self.casting = False
            self.character = True
            self.spell = []
            self.spelltarget = []
            self.skills = []
            self.target = ""
    def choice(self):
            # dependent on current health, status, stats of chars etc
            pass
    def drop(self, inventory):
            for loot in self.drop:
                    dropRoll = randint(1, 1000)
                    if dropRoll <= 1000 * self.drop(loot[0]):
                            return ("{} dropped {}!".format(self.name, loot.name))
                            loot.acquire(inventory, loot[1])


# Status effect data

negstatus_list = ["poison", "petrify", "paralyse", "blind", "burn", "frostbite", "death", "curse", "wither", "spellbind"]

def poison_status(schmuck):
    if schmuck.inflict["poison"] == True:
        schmuck.tick["poison"] == 19
        schmuck.inflict["poison"] = False
        poisonDamage = (schmuck.maxhp // 15) - ceil((schmuck.maxhp // 15) * schmuck.absorb["poisonDef"])
        damage(schmuck, poisonDamage)
    elif schmuck.tick["poison"] > 0:
        poisonDamage = (schmuck.maxhp // 15) - ceil((schmuck.maxhp // 15) * schmuck.resist[8])
        tick_damage(schmuck, poisonDamage)
        schmuck.tick[0] -= 1
        
def petrify_status(schmuck):
    if schmuck.inflict["petrify"] == True and schmuck.immune["petrify"] == False:
        schmuck.active = False
        schmuck.target = False
        schmuck.inflict["petrify"] = False
        for x in schmuck.tick:
                x = 0
        schmuck.tick["petrify"] = 1
    elif schmuck.tick["petrify"] == 1:
            pass
    
def para_status(schmuck):
    if schmuck.inflict["paralyse"] == True and schmuck.immune["paralyse"] == False:
        schmuck.active = False
        schmuck.tick["paralyse"] == 12
    elif schmuck.tick["paralyse"] > 0:
        schmuck.active = False
        schmuck.tick["paralyse"] -= 1
    elif schmuck.tick == 0 and (schmuck.tick["petrify"] + schmuck.tick["burn"]) == 0:
        schmuck.active = True

def blind_status(schmuck):
    if schmuck.inflict["blind"] == True and schmuck.immune["blind"] == False:
        schmuck.acc == 0
        schmuck.inflict["blind"] = False
        schmuck.tick["blind"] = 12
    elif schmuck.inflict["blind"] == False and schmuck.tick["blind"] > 0:
        schmuck.acc == 0    
        schmuck.tick -= 1    
    elif schmuck.inflict["blind"] == True and schmuck.immune["blind"] == True:
        schmuck.inflict["blind"] = False
        
def burn_status(schmuck):
    if schmuck.inflict["burn"] == True:
        schmuck.tick["burn"] == 6
        schmuck.inflict["burn"] = False
        schmuck.active = False
        fireDamage = (schmuck.maxhp // 5) - ceil((schmuck.maxhp // 5) * schmuck.absorb["fireResist"])
        damage(schmuck, poisonDamage)
    elif schmuck.tick["burn"] > 0:
        schmuck.active = False    
        fireDamage = (schmuck.maxhp // 5) - ceil((schmuck.maxhp // 5) * schmuck.absorb["fireResist"])
        tick_damage(schmuck, fireDamage)
        schmuck.tick["burn"] -= 1
    elif schmuck.tick["burn"] <= 0 and schmuck.tick == 0 and (schmuck.tick["petrify"] + schmuck.tick["burn"]) == 0:
        schmuck.active = True
        
def frost_status(schmuck):
    if schmuck.inflict["frostbite"] == True:
        schmuck.tick["frostbite"] == 150
        schmuck.inflict["frostbite"] = False
        schmuck.speed = 0.4(schmuck.speed)
        frostDamage = (schmuck.maxhp // 25) - ceil((schmuck.maxhp // 25) * schmuck.absorb["iceResist"])
        damage(schmuck, poisonDamage)
    elif schmuck.tick["frostbite"] > 0:  
        frostDamage = (schmuck.maxhp // 25) - ceil((schmuck.maxhp // 25) * schmuck.absorb["iceResist"])
        tick_damage(schmuck, fireDamage)
        schmuck.tick["frostbite"] -= 1
    elif schmuck.tick["frostbite"] == 0:
        schmuck.speed = 2.5(schmuck.speed)
        
def death_status(schmuck):
    if schmuck.alive == True:
        schmuck.alive == False


buff_list = []
status_dict = {
    "poison": poison_status,
    "petrify": petrify_status,
    "paralyse": para_status,
    "blind": blind_status,
    "burn": burn_status,
    "frostbite": frost_status,
    "death": death_status}

inflict_dict = [False, False, False, False, False, False, False]

def negstatus_check(character, negstatus_list, status_dict):
    for i in negstatus_list:
        if character.inflict[i] == True and character.ticks[i] == 0:
            return("{} inflicted with {}!".format(character.name, (status_list[effect]).upper()))
            status_dict[status_list[effect]]()
        else:
            pass


def wincon_check(party, enemy_party, victory, defeat):
    for life in party:
        casualties = 0
        if (life.alive == True or (life.tick_dict["petrify"] == 0)) == False:
            casualties += 1
    if casualties == len(party):
        defeat = True
    else:     
        for life in enemy_party:
            casualties = 0
            if life.alive == False or (life.active == True and life.tick_dict["petrify"] > 0) == False:
                casualties += 1
        if casualties == len(enemy_party):
            victory = True

def buff_check(character, buff_list, buff_dict):
    for i in range(1, len(buff_list)):
        buff = i - 1

def genstatus_check():
        pass

# status_dict[status_list[effect]]()
# elif character.inflict[effect] == False and character.tick[effect] > 0:
# pass
# status_dict[status_list[effect]]()

