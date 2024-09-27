class Character():
    def __init__(self) -> None:
        self.health = 100 # stat used to track whether the character is dead or not
        self.stamina = 75 # stat used for special physical moves
        self.mana = 50 # stat used for spells
        self.shield = 0 # stat used to track how much damage is blocked
        self.attack_value = 1 # stat used to track how much extra damage should be added to physical attacks
        self.magic_attack = 1 # stat used to track how much extra damage should be added to magic attacks
        self.thorns = 0 # stat used to track how much damage should be reflected back on the attacker
        self.name = "none yet"

    def takedamage(self, damage): # If this can be used for the enemy as well then maybe there is a means of inheritance, creating Parent and child classes? I'll have to look into it.
        """This is the method that causes the player to take damage, this could be used for the enemy or any other entity as well"""
        while damage > 0 < self.shield:
            if self.shield < damage:
                damage -= self.shield
                self.shield = 0
            self.health -= damage
            damage = 0
    
    def shield_gain(self, value):
        self.shield += value

    def attack(): # pass action object in and then use the attack object stats as a means to calculate the logic behind dealing damage, also pack enemy object so the game knows who to damage.
        pass