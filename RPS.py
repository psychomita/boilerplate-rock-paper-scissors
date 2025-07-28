import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    guess_table = {}
    for i in range(len(opponent_history) - 2):
        key = "".join(opponent_history[i:i+2])
        next_move = opponent_history[i + 2]
        if key in guess_table:
            guess_table[key][next_move] = guess_table[key].get(next_move, 0) + 1
        else:
            guess_table[key] = {next_move: 1}

    last_two = "".join(opponent_history[-2:])
    prediction = "R"
    if last_two in guess_table:
        prediction = max(guess_table[last_two], key=guess_table[last_two].get)

    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter_moves[prediction]
