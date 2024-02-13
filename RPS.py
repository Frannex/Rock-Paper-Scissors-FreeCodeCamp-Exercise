import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    counter = {'S': 'R', 'R': 'P', 'P': 'S'}
    guess = random.choice(['R', 'P', 'S'])

    if len(opponent_history) >= 4:
        last_opponent_play = opponent_history[-1]
        guess = counter[last_opponent_play]

        play_order = [''.join(opponent_history[k:k+4]) for k, v in enumerate(opponent_history[:-3])]
        potential_play = [''.join([*opponent_history[-3:], v]) for v in ['R', 'P', 'S']]
        sub_order = {k: play_order.count(k) for k in potential_play}

        frequent_play = max(sub_order, key=sub_order.get)[-1]
        guess = counter[frequent_play]

        if random.random() < 0.001: 
            guess = random.choice(['R', 'P', 'S'])

    return guess


