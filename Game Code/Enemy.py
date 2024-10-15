from Character import Character
class Enemy(Character):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.max_health = 100
        self.current_health = self.max_health
        self.max_mana = 50
        self.current_mana = self.max_mana
        self.max_stamina = 50
        self.current_stamina = self.max_stamina