import GameData
import main as main_game
    
def initiate_battle():
    """Use this to establish what the first turn will be when a battle begins"""
    global battle_conditions
    global turn_count
    turn_count = 0
    battle_conditions = True
    # reset player stats at the beginning of the battle

def turn_increment():
    """Used to increment the turn count to see how long the battle has gone for. Could be used for some enemy mechanics as well."""
    global turn_count
    turn_count += 1
    GameData.total_turns += 1

def trigger_start_turn_effects():
    """Automatically triggers any start of turn effects that the character may have applied to them"""
    pass

def trigger_end_turn_effects():
    """Automatically triggers any end of turn effects that the character may have applied to them"""
    pass

initiate_battle()
