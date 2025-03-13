import random

def player(prev_play, opponent_history=[]):
    # Keep track of opponent's move history
    if prev_play:
        opponent_history.append(prev_play)

    # If not enough history, play randomly
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    # Count frequency of opponent's past moves
    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counts[move] += 1

    # Predict opponent's next move based on frequency
    predicted = max(counts, key=counts.get)

    # Counter opponent's most frequent move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    
    return counter_moves[predicted]
