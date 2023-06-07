# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Playing cards
# 29/05/2023

# class Card():
#     """
#     A playing card
#     """
#     RANKS = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     SUITS = ["D", "H", "S", "C"]
#     NUMBER_VALUE = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
#                     "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,}
#     def __init__(self, rank, suits):
#         self.rank = rank
#         self.suits = suits

#     def __str__(self):
#         rep = f"{self.rank}:{self.suits}"
#         return rep
    
#     def return_card_value(self):
#         #value = None
#         try:
#             value = Card.NUMBER_VALUE[self.rank]
#             return value
#         except:
#             print("Value not in cards")

# card1 = Card(Card.RANKS[1], Card.SUITS[1])
# print(card1)
# value1 = card1.return_card_value()
# print(value1)

# card_one = Card(Card.SUITS[1], Card.RANKS[0])
# # print(card_one.suits)
# # print(card_one.rank)
# card_two = Card(Card.SUITS[2], Card.RANKS[6])
# #print(card_one)
# #print(card_two)
# #
# print(card_one)
# print(card_two)


# class Hand():
#     """
#     A hand of cards
#     """
#     def __init__(self):
#         self.cards = []

#     def __str__(self):
#         rep = ""
#         if self.cards:

#             for card in self.cards:
#                 rep += f"{str(card)} "
#         else:
#             rep = "<Empty Hand>"
#         return rep

#     def clear_hand(self):
#         self.cards = []

#     def add_card(self, card):
#         self.cards.append(card)

#     def give_card(self, card, other_hand):
#         self.cards.remove(card)
#         other_hand.add_card(card)

# my_hand = Hand()
# #print(my_hand)
# my_hand.add_card(card_one)
# #print(my_hand)

# my_hand.add_card(card_two)
# #print(my_hand)

# hand2 = Hand()
# #print(hand2)
# my_hand.give_card(card_one,hand2)
# #print(my_hand)
# #print(hand2)

# class Deck(Hand):
#     """
#     Deck of playing cards
#     """
#     def create_deck(self):
#         for suit in Card.SUITS:
#             for rank in Card.RANKS:
#                 self.add_card(Card(rank, suit))

#     def shuffle(self):
#         import random

#         random.shuffle(self.cards)

#     def deal(self, hands, per_hand=1):
#         for rounds in range(per_hand):
#             for hand in hands:
#                 if self.cards:
#                     top_card = self.cards[0]
#                     self.give_card(top_card, hand)
#                 else:
#                     print("Out of cards")

# def show_rules():
#     """
#     Take a text file with the rules in it and display it back to the user
#     """
#     try:
#         rules_file = open("rules.txt", "r")
#         lines = rules_file.readlines()
#         for line in lines:
#             print(line)
#     except:
#         print("Uh oh something went wrong!")


# my_deck = Deck()
# my_deck.create_deck()

# print(my_deck)
# print("***************************************")

# my_deck.shuffle()
# # print(my_deck)

# my_hand = Hand()
# dealer_hand = Hand()

#players = [my_hand, dealer_hand]
# print(my_hand)
# print(dealer_hand)
# print("*********************")
#show_rules()


#input("\n\nPress Enter to Exit\n")

class Card():
    """A Playing Card Object """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]
    SUITS = ["\u2663", "\u2665", "\u2666", "\u2660"]
    NUMBER_VALUE = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                    "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    
    def __init__(self, rank, suit) -> None:
        """
        Initialize class
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Make strings from initializer function
        """
        rep = f"{self.rank}:{self.suit}"
        return rep

    def return_card_value(self):
        """
        Add card number values to card ranks
        """
        try:
            value = Card.NUMBER_VALUE[self.rank]
            return value
        except:
            print("Value not in cards")

card1 = Card(Card.RANKS[1], Card.SUITS[1])
print(card1)
value1 = card1.return_card_value()
print(value1)
