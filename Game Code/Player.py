from Character import Character
from Actions import Actions
from Enemy import Enemy

class Player(Character):
    def __init__(self) -> None:
        super().__init__()
        self.max_health = 100
        self.current_health = self.max_health # stat used to track whether the character is dead or not
        self.max_stamina = 75 
        self.current_stamina = self.max_stamina # stat used for special physical moves
        self.max_mana = 50 
        self.current_mana = self.max_mana # stat used for spells
        self.actions = {
            "Hit" : Actions("Hit", mana_cost = 0, move_value = 5, stamina_cost = 5, move_type = "attack", target = "enemy"),
            "Block" : Actions("Block", mana_cost = 0, move_value = 10, stamina_cost = 10, move_type = "action", target = "self"),
            "Buff Thorns" : Actions("Reinforce", mana_cost = 0, move_value = 10, stamina_cost = 10, move_type = "buff", target = "self", stat = "thorns")
        }
    
    def move_selection(self):
        self.display_choices()
        user_input = input("\nSelect a move: ").lower()
        for Action in self.actions:
            if user_input == Action.name.lower():
                self.check_resources(Action)
                break
        else:
            print("Not a valid move...\n")
            self.move_selection()
    
    def reduce_resources(self, stamina_cost, mana_cost):
        self.current_stamina -= stamina_cost
        self.current_mana -= mana_cost
    
    def check_resources(self, Action):
        """Checks if the caster of the ability has enough stamina or mana to cast the move. Prompts user to select a different move if unable to use that move."""
        move_can_be_casted = True
        if Action.stamina_cost > self.stamina:
            move_can_be_casted = False
            print("Not enough stamina")
        if Action.mana_cost > self.mana:
            move_can_be_casted = False
            print("Not enough stamina")
        if move_can_be_casted == True:
            self.reduce_resources(Action.stamina_cost, Action.mana_cost)
            self.action(Action, enemy)
        else:
            print("Select a different move...")
            self.move_selection()

    def action(self, Action, Target): # pass action object in and then use the attack object stats as a means to calculate the logic behind dealing damage, also pass enemy object so the game knows who to damage.
        print(f"Performing {Action.name} on {Target.name}!")
        if Action.type == "attack":
            Target.takedamage(damage = (Action.move_value + self.attack_value))
    
    # This may be able to be moved to the Game Handler or Game Logic class instead of the Player Class, or the Player Controller Class
    def display_choices_format(self, Move):
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
        
    def turn(self):
        pass


        
player = Player()
enemy = Enemy(name = "Goblin")
player.buff(player.actions["Buff Thorns"])
# player.move_selection()