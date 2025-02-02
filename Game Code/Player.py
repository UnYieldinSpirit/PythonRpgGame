from Character import Character
from Actions import Actions
from Enemy import Enemy

class Player(Character):
    def __init__(self, enemy) -> None:
        super().__init__()
        enemy = enemy
        self.name = "Self"
        self.max_health = 100
        self.current_health = self.max_health # stat used to track whether the character is dead or not
        self.max_stamina = 75 
        self.current_stamina = self.max_stamina # stat used for special physical moves
        self.max_mana = 50
        self.current_mana = self.max_mana # stat used for spells
        self.health_holder = self.current_health
        self.actions = {
            "Hitter" : Actions(name = "Hit", mana_cost = 0, move_value = 5, stamina_cost = 5, move_type = "attack", target = "enemy"),
            "Block" : Actions(name = "Block", mana_cost = 0, move_value = 10, stamina_cost = 10, move_type = "block", target = "self"),
            "Buff Thorns" : Actions(name = "Reinforce", mana_cost = 0, move_value = 10, stamina_cost = 10, move_type = "buff", target = "self", stat = "thorns"),
            "Cast Fireball" : Actions(name = "Cast Fireball", mana_cost = 30, move_value = 30, stamina_cost = 15, move_type = "attack", target = "enemy"),
        }
    
    def move_selection(self):
        """Intakes the user's choice and from there it causes the action to be performed"""
        self.display_choices()
        user_input = input("\nSelect a move: ").lower()
        for Action in self.actions:
            if user_input == self.actions.get(Action).name.lower():
                self.check_resources(self.actions.get(Action))
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
        if Action.stamina_cost > self.current_stamina:
            move_can_be_casted = False
            print("Not enough stamina")
        if Action.mana_cost > self.current_mana:
            move_can_be_casted = False
            print("Not enough mana")
        if move_can_be_casted == True:
            self.reduce_resources(Action.stamina_cost, Action.mana_cost)
            if Action.target == "enemy":
                self.action(Action, enemy)
            if Action.target == "self":
                self.action(Action, self)
        else:
            print("\nSelect a different move...\n")
            self.move_selection()

    def action(self, Action, Target): # pass action object in and then use the attack object stats as a means to calculate the logic behind dealing damage, also pass enemy object so the game knows who to damage.
        print(f"\nPerforming {Action.name} on {Target.name}!")
        if Action.type == "attack":
            Target.take_damage(damage = (Action.move_value + self.attack_value))
        if Action.type == "block":
            Target.shield_gain(Action.move_value)
        if Action.type == "buff":
            Target.buff(Action)
    
    def display_player_stats(self):
        print(f"Health: {self.current_health}/{self.max_health}")
        print(f"Stamina: {self.current_stamina}/{self.max_stamina}")
        print(f"Mana: {self.current_mana}/{self.max_mana}\n")
    
    def display_choices_format(self, Move):
        """Used as a means to format the choices that will be displayed for the user to select for their characters in battle"""
        option = f"{Move.name} - "
        if Move.stamina_cost > 0 and Move.mana_cost > 0:
            option += f"stamina: {Move.stamina_cost}, mana: {Move.mana_cost}"
        elif Move.stamina_cost > 0:
            option += f"stamina: {Move.stamina_cost}"
        elif Move.mana_cost > 0:
            option += f"mana: {Move.mana_cost}"
        return option

    def display_choices(self):
        for i in self.actions:
            print(f"{self.display_choices_format(Move = self.actions.get(i))}")
        
    def turn(self):
        self.display_player_stats()
        player.move_selection()

player = Player()
# player.buff(player.actions["Buff Thorns"])