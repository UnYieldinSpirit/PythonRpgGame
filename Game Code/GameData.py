# global data that is needed through all of the classes and mechanics
total_turns = 0
weakness = .25
broken = .50
total_score = 0
max_potential_score = 5000
current_potential_score = max_potential_score

def reduce_potential_score():
    import BattlePhase
    current_potential_score -= (BattlePhase.player_health_start - BattlePhase.player.current_health)
    current_potential_score -= (BattlePhase.turn_count * 4)
