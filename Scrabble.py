"""
In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!
"""
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
player_to_points = {}

letters.append(" ")
points.append(0)
letter_to_points = dict(zip(letters, points))
print(letter_to_points)

def score_word(word):
    """
        this fonction calculate the point based on words.
        Parameters:
        word : word that we choise to calculate points (str)
        Returns:
        point_total = total point of the world we choise (int)

    """
    point_total = 0
    for letter in word:
        letter = letter.upper()
        point_total += letter_to_points.get(letter, 0)
    return point_total

# Example usage:
word ="BROWNIE"
brownie_points = score_word(word)
print(f"Score of {word} is:", brownie_points)

player_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
    'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points
#print(player_to_points)
print("Current Standings:")
for player, points in player_to_points.items():
    print(f"{player}: {points} points")
