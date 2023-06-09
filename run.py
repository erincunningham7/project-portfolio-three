# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Playing cards
# 29/05/2023

import random


class Card():
    """
    A playing card object that creates suits,
    ranks and their respective number values
    """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]
    SUITS = ["\u2663", "\u2665", "\u2666", "\u2660"]
    NUMBER_VALUE = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    ACE_VALUE = 11

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
        except ValueError:
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

        # Determine if there is an ace in the hand
        contains_ace = False
        for card in self.cards:
            if card.return_card_value() == Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and total > 21:
            total -= 10

        return total


class Deck(Hand):
    """
    This class creates a full deck of playing cards and
    inherits from the hand class
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
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        """
        Deal cards
        """
        for _ in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't deal anymore. Out of cards")


def show_rules():
    """
    A function that uses file I/O to read a
    txt file and show the rules on the screen
    """
    text_file = open("rules.txt", "r")
    for line in text_file:
        print(line)
    text_file.close()


def compare_score(score1, score2):
    """"
    Compare the score values of a hand and decide the winner
    """
    if score1 == score2:
        return "It's a draw!"
    elif score2 == 21:
        return "Computer wins! Blackjack!!!"
    elif score1 == 21:
        return "Player wins! Blackjack!!!"
    elif score1 > 21:
        return "Player went bust! Player loses! Computer wins!"
    elif score2 > 21:
        return "Computer went bust! Computer loses! Player wins!"
    elif score1 > score2:
        return "Player closest to 21. Player wins!"
    else:
        return "Computer closest to 21. Computer wins!"


def ask_yes_no(question):
    """
    A function that only allows the user to answer "y" or "n"
    """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def play_game():
    """
    A function that allows the user to play a
    game of blackjack against the computer
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
    print(f"Players Hand: {player_hand}")
    print(f"Computers Hand: {computer_hand}")

    player_score = player_hand.hand_total()
    computer_score = computer_hand.hand_total()
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    if player_score > 21:
        is_game_over = True
    else:
        player_hit = ask_yes_no("Type 'y' to hit or 'n' to stand: \n")
        if player_hit == 'y':
            blackjack_deck.deal([player_hand])
        else:
            is_game_over = True

    while not is_game_over:
        player_score = player_hand.hand_total()
        computer_score = computer_hand.hand_total()

        print(f"Player Hand: {player_hand}")
        print(f"Player Score: {player_score}")

        print(f"Computer Hand: {computer_hand}")
        print(f"Computer Score: {computer_score}")

        if player_score > 21:
            is_game_over = True
        else:
            player_hit = ask_yes_no("Type 'y' to hit or 'n' to stand: \n")
            if player_hit == 'y':
                blackjack_deck.deal([player_hand])
            else:
                is_game_over = True

    while computer_score < 17:
        blackjack_deck.deal([computer_hand])
        computer_score = computer_hand.hand_total()

    print(f"Player cards: {player_hand}")
    print(f"Player Hand total: {player_score}")
    print(f"Computer Cards: {computer_hand}")
    print(f"Computer Hand total: {computer_score}")
    result = compare_score(player_score, computer_score)
    print(result)
    # Clear the deck for the next round
    blackjack_deck.clear()
    player_hand.clear()
    computer_hand.clear()


def print_menu():
    """
    Print User interface and game art
    """
    logo = """
        .------.            _     _            _    _            _
        |A_  _ |.          | |   | |          | |  (_)          | |
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |
              `------'                           |__/
    """
    print(logo)
    print("Press 1 to view the rules.")
    print("Press 2 to play the game.")
    print("Press 0 to Quit the game.")

# Creating the user menu allowing the user to interact with the game


choice = None
while choice != "0":
    print_menu()
    choice = input("Choose an option: \n")
    if choice == "0":
        print("Thanks for playing!")
    elif choice == "1":
        show_rules()
        input("Press enter to continue \n")
    elif choice == "2":
        play_again = True
        play_game()
        while play_again:
            play = ask_yes_no("Type 'y' to play again or 'n' to quit\n")
            if play == 'y':
                play_game()
            else:
                play_again = False
    else:
        print("Sorry that isnt a valid choice")
