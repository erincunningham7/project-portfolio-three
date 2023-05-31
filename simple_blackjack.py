import random

user_cards = []
computer_cards = []

def deal_card():
    """
    Return a random card from a deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#print(deal_card())

for round in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# print(user_cards)
# print(computer_cards)

def calculate_score(card_hand):
    if 11 in card_hand and 10 in card_hand and len(card_hand) == 2:
        return 0
    if 11 in card_hand and sum(card_hand) > 21:
        card_hand.remove(11)
        card_hand.append(1)
    return sum(card_hand)

input("\n Press enter to exit")