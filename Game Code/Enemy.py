from Character import Character
import Player as Player

class Enemy(Character):
    def __init__(self) -> None:
        super().__init__()
        self.name
        self.max_health
        self.current_health = self.max_health
        self.max_mana
        self.current_mana = self.max_mana
        self.max_stamina
        self.current_stamina = self.max_stamina
        self.opposition = player
