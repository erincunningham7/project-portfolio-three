import random

user_cards = []
computer_cards = []

is_game_over = False

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

def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins"
    elif user_score == 0:
        return "Player wins"
    elif user_score > 21:
        return "User went bust! Computer wins"
    elif computer_score > 21:
        return "Computer went bust! User wins"
    elif user_score > computer_score:
        return "User wins"
    else:
        return "Computer wins"

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Player cards {user_cards} player score {user_score}")
print(f"Computers first card {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    user_hit = input("Would you like another card? y/n")
    if user_hit == "y":
        user_cards.append(deal_card())
    else:
        is_game_over = True
    
print(is_game_over)
print(user_cards)
print(is_game_over)

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(user_score)
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_hit = input("Would you like another card? y/n")
        if user_hit == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Player score is {calculate_score(user_cards)}")
print(f"Computer score is {calculate_score(computer_cards)}")
result = compare_score(user_score, computer_score)
print(result)

input("\n Press enter to exit")