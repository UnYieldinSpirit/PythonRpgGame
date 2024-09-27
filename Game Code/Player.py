from Character import Character
from Actions import Actions
class Player(Character):
    def __init__(self) -> None:
        super().__init__()
        self.actions = {
            Actions("Hit", mana_cost = 0, move_value = 5, stamina_cost = 5, move_type = "attack"),
            Actions("Block", mana_cost = 0, move_value = 10, stamina_cost = 10, move_type = "action"),
            Actions("Punish", mana_cost = 15, stamina_cost = 10, move_value = 20 , move_type = "spell"),
            Actions("Cast Fire Ball", mana_cost = 15, stamina_cost = 10, move_value = 20 , move_type = "spell")
        }

    def display_choices_format(Move):
        option = f"{Move.name} - "
        if Move.stamina_cost > 0:
            option += f"stamina: {Move.stamina_cost} "
        if Move.mana_cost > 0:
            option += f"mana: {Move.mana_cost} "
        return option
    
    def display_choices(self):
        for i in self.actions:
            print(f"{Player.display_choices_format(Move = i)}")
            # print(f"{i.name} - mana: {i.mana_cost}, stamina: {i.stamina_cost}")
        
me = Player()
me.display_choices()