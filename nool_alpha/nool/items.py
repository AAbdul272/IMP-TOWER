


import status
from status import *


# Weapon template

weaponstats_template = {"bluntAttack": 0, "pierceAttack": 0, "slashAttack": 0, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 0, "AttackSpeed": 1, "STRscale": 0, "DEXscale": 0, "INTscale": 0}

# Weapon stat data

oak_stats = {"bluntAttack": 7, "pierceAttack": 0, "slashAttack": 0, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 11, "AttackSpeed": 1, "STRscale": 1.0, "DEXscale": 0, "INTscale": 0}

grimoire_stats = {"bluntAttack": 5, "pierceAttack": 0, "slashAttack": 0, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 8, "AttackSpeed": 1.4, "STRscale": 0.3, "DEXscale": 1.5, "INTscale": 0}

pike_stats = {"bluntAttack": 0, "pierceAttack": 11, "slashAttack": 0, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 0, "AttackSpeed": 1.2, "STRscale": 0, "DEXscale": 0, "INTscale": 0}

mace_stats = {"bluntAttack": 10, "pierceAttack": 0, "slashAttack": 0, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 0, "AttackSpeed": 1.3, "STRscale": 0, "DEXscale": 0, "INTscale": 0}

sabre_stats = {"bluntAttack": 0, "pierceAttack": 0, "slashAttack": 8, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 0, "AttackSpeed": 1.3, "STRscale": 0, "DEXscale": 1.2, "INTscale": 0}

# Sidearm stat data

shield_stats = {"bluntAttack": 4, "pierceAttack": 0, "slashAttack": 3, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 0, "AttackSpeed": 1, "STRscale": 0.7, "DEFboost": 1.7}

dagger_stats = {"bluntAttack": 0, "pierceAttack": 5, "slashAttack": 0, "darkAttack": 0, "fireAttack": 0, "iceAttack": 0, "boltAttack": 0, "magicAttack": 0, "AttackSpeed": 1.8, "STRscale": 0, "DEXscale": 0, "INTscale": 2.0}

# Weapon class instancing

# example = Weapon("", 9, _stats, "")

# Weapon 

oak_staff = Weapon("Oak Staff", 9, oak_stats, "Weapon")

grimoire = Weapon("Grimoire", 9, grimoire_stats, "Weapon")

sabre = Weapon("Sabre", 9, sabre_stats, "Weapon")
 
pike = Weapon("Pike", 9, pike_stats, "Weapon")

mace = Weapon("Mace", 9, mace_stats, "Weapon")

# Sidearm

dagger = Weapon("Dagger", 9, dagger_stats, "Sidearm")

shield = Weapon("Issued Shield", 9, shield_stats, "Sidearm")

# Armor template



# Helmets

issued_cap  

# Armor



# Gloves




# All Classes and vital class data

mage = {"Class": "Mage", "Weapon": grimoire, "Sidearm": "N/A", "Command": "Magic"}

summoner = {"Class": "Summoner", "Weapon": oak_staff, "Sidearm": "N/A", "Command": "Summons"}

rogue = {"Class": "Rogue", "Weapon": sabre, "Sidearm": dagger, "Command": "Hustle"}

dragoon = {"Class": "Dragoon", "Weapon": pike, "Sidearm": "N/A", "Command": "D. Arts"}

knight = {"Class": "Knight", "Weapon": mace, "Sidearm": shield, "Command": "C. Arts"}

