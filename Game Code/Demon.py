from Enemy import Enemy
class Demon(Enemy):
    def __init__(self) -> None:
        self.name = "Demon"
        self.max_health = 250
        self.max_mana = 20
        self.max_stamina = 300
        super().__init__()