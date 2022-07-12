class TestGoblin(Monster):
        def __init__(self, name, level, drop):
                self.name = name
                self.level = level
                self.drop = drop
                exp_drop = 21 * level
                self.maxhp = ceil(13 + 10(self.level))
                self.maxmp = ceil(7 + 5(self.level))
                self.str = ceil(2 + 2(self.level))
                self.dex = ceil(2 + 2(self.level))
                self.int = ceil(2 + 2(self.level))
                self.hp = self.maxhp
                self.mp = self.maxmp
                self.inventory = {gobbo_cocktail: 3}
                self.active = True
                self.alive = True
        def choice(self, party, enemy_party):
                if self.hp >= 0.5 * self.maxhp:
                        weak1_target(self, enemy_party, attack)
                elif self.hp <= 0.5 and self.inventory[gobbo_cocktail] > 0:
                        gobbo_cocktail.use_item(self, self.inventory)
                else:
                        flee(self, enemy_party)

def weak1_target(monster, party, ability):
        priority_list = []
        for target in party:
                analysedHP = target.hp
                priority_list.append(analysedHP)
        priority_list.sort()
        priority = priority_list[0]
        for target in party:
                if target.hp == priority:
                        ability(target)
                        pass
