from Character import Character
class Enemy(Character):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name