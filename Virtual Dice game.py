import random
def roll_dice():
    return random.randint(1, 6)
def play_round(players, scores):
    round_results = {}
    for player in players:
        roll = roll_dice()
        print(f"{player} rolled: {roll}")
        round_results[player] = roll
        while roll == 6:
            print(f"{player} rolled a 6! Rolling again...")
            roll = roll_dice()
            print(f"{player} rolled: {roll}")
            round_results[player] = max(round_results[player], roll)

    max_roll = max(round_results.values())
    winners = [player for player, roll in round_results.items() if roll == max_roll]
    if len(winners) == 1:
        print(f"Winner of this round: {winners[0]}\n")
        scores[winners[0]] += 1
    else:
        print(f"It's a tie between: {', '.join(winners)}\n")

    return scores
def display_leaderboard(scores):
    print("\nLeaderboard:")
    for player, wins in scores.items():
        print(f"{player}: {wins} wins")
def main():
    num_players = int(input("Enter the number of players (2-4): "))
    while num_players < 2 or num_players > 4:
        print("Invalid number of players. Please enter between 2 and 4.")
        num_players = int(input("Enter the number of players (2-4): "))

    players = [input(f"Enter name for Player {i + 1}: ") for i in range(num_players)]
    scores = {player: 0 for player in players}

    rounds = int(input("Enter number of rounds: "))
    for _ in range(rounds):
        print("\nNew Round!")
        scores = play_round(players, scores)
        display_leaderboard(scores)

    overall_winner = max(scores, key=scores.get)
    print(f"\nCongratulations {overall_winner}! You are the overall winner!")
if __name__ == "__main__":
    main()