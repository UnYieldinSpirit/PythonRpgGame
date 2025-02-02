# global data that is needed through all of the classes and mechanics
from Demon import Demon
import random

total_turns = 0
weakness = .25
broken = .50
total_score = 0
max_potential_score = 5000
current_potential_score = max_potential_score

global enemy_list
enemy_list = []

enemy_list.append(Demon())

for i in enemy_list:
    print(i.name)

def reduce_potential_score():
    import BattlePhase
    current_potential_score -= (BattlePhase.player_health_start - BattlePhase.player.current_health)
    current_potential_score -= (BattlePhase.turn_count * 4)

def enemy_selection():
    enemy = enemy_list[random.randint(0, (enemy_list.len() - 1))]
    return enemy