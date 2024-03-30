import random

# This line creates a set with 6 random numbers
lottery_numbers = (random.sample(list(range(22)),6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

winners_list = []
highest = 0
name = ""
for player in players:
   winners_list.append((player.get("name"),set(player.get("numbers")).intersection(set(lottery_numbers)).__len__() * 100))
   score = set(player.get("numbers")).intersection(set(lottery_numbers)).__len__() * 100
   if score > highest:
      highest = score
      name = player.get("name")


#print(winners_list)   
#f = lambda tup: tup[1]
#winners_list.sort(f,reverse=True)
#print(winners_list)   
#print([ f(winner) for winner in winners_list ] )
print(f"{name} won {highest}")


