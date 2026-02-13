# game_score.py
# Input Collection
name = input("Enter player's name: ")

# Numeric Input Processing
games_played = int(input("Enter number of games played: "))

# Score Data Entry
total_score = int(input("Enter total score: "))

# Computation
average_score = total_score / games_played

# Output Display
print("\nPlayer:", name)
print("Games Played:", games_played)
print("Total Score:", total_score)
print("Average Score:", average_score)
