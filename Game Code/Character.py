class Character():
    def __init__(self) -> None:
        self.shield = 0 # stat used to track how much damage is blocked
        self.attack_value = 0 # stat used to track how much extra damage should be added to physical attacks
        self.magic_attack = 0 # stat used to track how much extra damage should be added to magic attacks
        self.thorns = 0 # stat used to track how much damage should be reflected back on the attacker
        self.turnSkip = False

        # negative effects listed below
        self.burn = 0
        self.hasBurn = False
        self.cold = 0 # future debuff that will cause the character to freeze and miss a turn
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
        """This method handles the increasing of whatever stat is affected by the Action"""
        self.__setattr__(Action.stat, Action.move_value + self.__getattribute__(Action.stat))

    def debuff(self, Action):
        """This method handles the decreasing of whatever stat is affected by the Action"""
        self.__setattr__(Action.stat, self.__getattribute__(Action.stat) - Action.move_value)
        
    def shield_gain(self, value):
        """Method used to increase the amount of shield that the character currently has"""
        self.shield += value
    
    def set_shield(self):
        """Method used to reset the shield of the character back to the predefined number"""
        self.shield = 0 # a class will have recurring shield when they start their turn

    def stamina_gain(self, value):
        """Used to increase the stamina that the character has by the value that is passed into it"""
        self.current_stamina += value
        if self.current_stamina > self.max_stamina:
            self.current_stamina = self.max_stamina

    def action(self, Action, Target): # pass action object in and then use the attack object stats as a means to calculate the logic behind dealing damage, also pass enemy object so the game knows who to damage.
        """Character performs an action on a passed in Target, effect changes depending on the action's parameters"""
        print(f"Performing {Action.name} on {Target.name}!")
        if Action.type == "attack":
            Target.takedamage(Action.move_value + self.attack_value)

    def trigger_burn(self):
        """Character takes damage based on the burn stat"""
        self.take_damage(self.burn)
        self.burn -= 1
        if self.burn == 0: # if the amount of burn falls to or below 0, then the character loses the hasBurn variable, preventing this method from running
            self.hasBurn = False

    def trigger_freeze(self):
        """Character becomes frozen, causing their turn to be skipped"""
        self.isFrozen = True
        self.turnSkip = True
        self.cold = 0

    def start_turn_effects(self):
        """Triggers the start of turn effects on the Character afflicted"""
        if self.cold >= 10:
            self.trigger_freeze()
        self.stamina_gain(value = self.stamina_replenish) 
    
    def end_turn_effects(self):
        """Triggers the end of turn effects on the Character afflicted"""
        if self.hasBurn == True:
            self.trigger_burn()