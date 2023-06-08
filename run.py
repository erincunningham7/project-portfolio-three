# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Playing cards
# 29/05/2023

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

class Hand():
    """
    A hand of playing cards
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += f"{str(card)} \t"
        else:
            rep = "<EMPTY>"
        return rep

    def clear(self):
        """
        Emptying every hand and deck when initially called
        """
        self.cards = []

    def add(self, card):
        """
        Give card to hand when game begins
        """
        self.cards.append(card)

    def give(self, card, other_hand):
        """
        Give cards to both players
        """
        self.cards.remove(card)
        other_hand.add(card)

    def hand_total(self):
        """
        Return the total value of cards in the hand
        """
        total = 0
        for card in self.cards:
            total += card.return_card_value()
        return total
 
class Deck(Hand):
    """
    This class creates a full deck of playing cards
    """
    def create_deck(self):
        """
        Loop through the suits and ranks, create cards and add them to the deck
        """
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """
        Use the random module and built in shuffle method to shuffle the deck
        """
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        """
        Deal cards
        """
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't deal anymore. Out of cards")

card1 = Card(Card.RANKS[1], Card.SUITS[1])

def show_rules():
    """ A function that uses file I/O to read a txt file and show the rules on the screen"""
    text_file = open("rules.txt", "r")
    for line in text_file:
        print(line)
    text_file.close()

#show_rules()

def play_game():
    """
    A function that allows the user to play a game of blackjack against the computer
    """
    blackjack_deck = Deck()
    blackjack_deck.create_deck()
    blackjack_deck.shuffle()

    # Flag to end the game
    is_game_over = False

    # Create player hand and computer hand
    player_hand = Hand()
    computer_hand = Hand()

    players = []
    players.append(player_hand)
    players.append(computer_hand)

    blackjack_deck.deal(players, 2)
    print(player_hand)
    print(computer_hand)

    player_score = player_hand.hand_total()
    computer_score = computer_hand.hand_total()
    print(player_score)
    print(computer_score)


play_game()
   
