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

print(user_cards)
print(computer_cards)