class Actions():
    """Models the actions that a character can take into a class structure for easier access"""
    def __init__(self, name, mana_cost, move_value, stamina_cost, move_type, target, stat = None) -> None:
        self.name = name
        self.mana_cost = mana_cost
        self.move_value = move_value
        self.stamina_cost = stamina_cost
        self.type = move_type
        self.target = target
        self.stat = stat

    # atk_value - the amount of damage/heals/shield/etc. that the move provides
    # stamina_cost & mana_cost - the amount of stamina/mana the move will cost
    # activation - whether it is a single instance move or a passive move that will happen at the end or beginning of every turn