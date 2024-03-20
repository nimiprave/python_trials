lottery_numbers = {13, 21, 22, 5, 8}

players = [
{
    'name': 'P1',
    'numbers': {1, 2, 3, 4, 5}
},
{
    'name': 'P2',
    'numbers': {6, 7, 8, 4, 5}
}

]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

player_1_result = len(players[0]['numbers'].intersection(lottery_numbers))
player_2_result = len(players[1]['numbers'].intersection(lottery_numbers))
print(f"Player {players[0]['name'] } got {player_1_result} numbers right")
print(f"Player {players[1]['name'] } got {player_2_result} numbers right")