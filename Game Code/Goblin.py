from Enemy import Enemy
from Actions import Actions
class Goblin(Enemy):
    def __init__(self, name, rank):
        super().__init__(name)
        self.name = name
        self.max_health = 70
        self.max_stamina = 30
        self.max_mana = 0
        self.rank = rank
        self.stamina_regen_rate = 2
        self.actions = {
            "Smack" : Actions(name = "Smack", mana_cost = 0, move_value = 7, stamina_cost = 5, move_type = "attack", target = "enemy"),
            "Block" : Actions(name = "Block", mana_cost = 0, move_value = 10, stamina_cost = 10, move_type = "block", target = "self"),
            "Heavy Swing" : Actions(name = "Heavy", mana_cost = 0, move_value = 14, stamina_cost = 15, move_type = "attack", target = "enemy")
        }
    
    def golbin_behavior(self):
        if (self.current_health > self.current_health * .25) and (self.current_stamina >= self.actions.get("Heavy Swing").stamina_cost):
            self.action(self.actions.get("Heavy Swing"), self.opposition)
        pass

    def Test(self):
        print(self.actions.get("Heavy Swing").move_value)
    