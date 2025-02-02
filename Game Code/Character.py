class Character():
    def __init__(self) -> None:
        self.shield = 0 # stat used to track how much damage is blocked
        self.attack_value = 0 # stat used to track how much extra damage should be added to physical attacks
        self.magic_attack = 0 # stat used to track how much extra damage should be added to magic attacks
        self.thorns = 0 # stat used to track how much damage should be reflected back on the attacker
        self.level = 1
        self.turnSkip = False
        self.stamina_regen_rate = 3

        # debuffs listed below
        self.burn = 0 # debuff that will cause the character to take some end of turn damage
        self.hasBurn = False
        self.cold = 0 # debuff that will cause the character to freeze and miss a turn
        self.isFrozen = False

    def take_damage(self, damage): # If this can be used for the enemy as well then maybe there is a means of inheritance, creating Parent and child classes? I'll have to look into it.
        """This is the method that causes the player to take damage, this could be used for the enemy or any other entity as well"""
        damage -= self.shield
        if self.shield < 0:
            self.shield = 0
        elif damage < 0:
            damage = 0
        self.current_health -= damage

    def buff(self, Action):
        self.__setattr__(Action.stat, Action.move_value + self.__getattribute__(Action.stat))

    def debuff(self, Action):
        self.__setattr__(Action.stat, self.__getattribute__(Action.stat) - Action.move_value)
        
    def shield_gain(self, value):
        self.shield += value
    
    def set_shield(self):
        self.shield = self.shield_standard # a class will have recurring shield when they start their turn
    
    def move_selection(self):
        pass
    
    def check_resources(self, Action):
        """Checks if the caster of the ability has enough stamina or mana to cast the move. Prompts user to select a different move if unable to use that move."""
        move_can_be_casted = True
        if Action.stamina_cost > self.current_stamina:
            move_can_be_casted = False
            print("Not enough stamina")
        if Action.mana_cost > self.current_mana:
            move_can_be_casted = False
            print("Not enough stamina")
        if move_can_be_casted == True:
            self.action()
        else:
            print("Select a different move...")
            self.move_selection()

    def action(self, Action, Target): # pass action object in and then use the attack object stats as a means to calculate the logic behind dealing damage, also pass enemy object so the game knows who to damage.
        print(f"Performing {Action.name} on {Target.name}!")
        self.check_resources(Action.mana_cost, Action.stamina_cost)
        if Action.type == "attack":
            Target.takedamage(Action.move_value + self.attack_value)
        if Action.type == "buff":
            break

    def trigger_burn(self):
        self.take_damage(self.burn)
        self.burn -= 1
        if self.burn == 0:
            self.hasBurn = False

    def trigger_freeze(self):
        self.isFrozen = True
        self.turnSkip = True
        self.cold = 0

    def start_turn_effects(self):
        if self.cold >= 10:
            self.trigger_freeze()
    
    def end_turn_effects(self):
        if self.hasBurn == True:
            self.trigger_burn()
        if self.cold < 10:
            self.isFrozen = False
            