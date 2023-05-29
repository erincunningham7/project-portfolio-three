# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Playing cards
# 29/05/2023

class Card(object):
    """
    A playing card
    """
    RANKS = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["D", "H", "S", "C"]
    def __init__(self, rank, suits):
        self.rank = rank
        self.suits = suits

    def __str__(self):
        rep = f"{self.rank}:{self.suits}"
        return rep

card_one = Card(Card.SUITS[1], Card.RANKS[0])
# print(card_one.suits)
# print(card_one.rank)
card_two = Card(Card.SUITS[2], Card.RANKS[6])
#print(card_one)
#print(card_two)

class Hand(object):
    """
    A hand of cards
    """
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        rep = ""
        if self.cards:
            
            for card in self.cards:
                rep += f"{str(card)} "
        else:
            rep = "<Empty Hand>"
        return rep
    
    def clear_hand(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def give_card(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add_card(card)
