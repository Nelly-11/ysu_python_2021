"""
This is the homework for the following topics
    - data types
    - control flows
    - math, random modules
Fill your from next line after # Answer:
"""

###################
# Task 1:
# Create and print 2 sets: ranks - ranks of cards; suits - suits of cards
# Answer:

ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", 'ace'}

suits = {
    "spades",
    "diamonds",
    "clubs",
    "hearts"
}

print(ranks)
print(suits)
###################

###################
# Task 2:
# Creat and print a list of tuples: deck - deck of 52 cards, using ranks and suits sets:
# [("2", "spades"), ("3", "spades"),...]
# Hint: use nested loops
# Answer:

deck = [(rank, suit) for rank in ranks for suit in suits]
print(deck)

deck = []
for suit in suits:
    for rank in ranks:
        deck.append((rank,suit))

print(deck)
###################
###################
# Task 3:
# Print the length of deck
# Print if it is equal to 52
# Answer:

length_of_deck = len(deck)
print(length_of_deck)
print(length_of_deck==52)

###################
###################
# Task 4:
# Print top card of the deck
# Shuffle the deck of of cards
# Print top card of the deck
# Hint: use random module
# Answer:

from random import shuffle

print(deck[0])
shuffle(deck)
print(deck[0])

###################
###################
# Task 5:
# Create hand_values dictionary of ranks to soft hand and hard hand value: {rank: (soft_hand, hard_hand)}
# Print the result
# Example: {"ace": (1,11), "2": (2,2),...}
# Hint: use this logic - for ace if is (1,11) for number it is the the face value for the rest it is 10
# Answer:

hand_values = {}

for rank in ranks:
    if rank == "ace":
        hand_values[rank] = (1, 11)
    elif rank.isnumeric():
        hand_values[rank] = (int(rank), int(rank))
    else:
        hand_values[rank] = (10, 10)

print(hand_values)
###################
