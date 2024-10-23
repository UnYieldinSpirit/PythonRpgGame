import GameController
from main import player
from main import enemy

def initiate_battle():
    """Use this to establish what the first turn will be when a battle begins"""
    global battle_conditions
    global turn_count
    global enemy
    global player_health_battle_start
    player_health_battle_start = player.current_health
    from main import enemy as enemy
    turn_count = 0
    battle_conditions = True
    # reset player stats at the beginning of the battle

def turn_increment():
    """Used to increment the turn count to see how long the battle has gone for. Could be used for some enemy mechanics as well."""
    global turn_count
    turn_count += 1
    GameController.total_turns += 1

def trigger_start_turn_effects():
    """Automatically triggers any start of turn effects that the character may have applied to them"""
    player.start_turn_effects()
    enemy.start_turn_effects()

def trigger_end_turn_effects():
    """Automatically triggers any end of turn effects that the character may have applied to them"""
    player.end_turn_effects()
    enemy.end_turn_effects()

def check_battle_conditions():
    global battle_end_message
    if player.current_health <= 0:
        return False
    elif enemy.current_health <= 0:
        return False
    else:
        return True
    
def battle():
    print("BATTLE BEGIN\n")
    while check_battle_conditions() == True:
        player.turn()
        enemy.deliberate()
