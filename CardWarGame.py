print "Insert player1 name"
print "Insert Player2 name"

import random

def shuffled_deck():
    basic_deck = range (2, 15) * 4
    random.shuffle(basic_deck)
    return basic_deck

deck = shuffled_deck()
def player_turn 


# player_turn: takes in a player name, player_name, and draws/removes a card
# from the deck, prints "user drew card x", and returns the value
#input: player_name, string
#output: string
