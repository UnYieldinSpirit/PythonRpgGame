import main as main_code
import GameData
class BattlePhase():
    def __init__(self) -> None:
        self.turn_count = 0
        
    def initiate_battle(self):
        """Use this to establish what the first turn will be when a battle begins"""
        self.turn_count = 0

    def turn_increment(self):
        """Used to increment the turn count to see how long the battle has gone for. Could be used for some enemy mechanics as well."""
        self.turn_count += 1
        GameData.total_turns += 1

    def trigger_start_turn_effects(self, character):
        """Automatically triggers any start of turn effects that the character may have applied to them"""
        character.setshield()

    def trigger_end_turn_effects(self, character):
        """Automatically triggers any end of turn effects that the character may have applied to them"""
        pass