import GameData
import main as main_game
import Player as player

turn_count
battle_conditions

def initiate_battle_first(player, enemy):
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
