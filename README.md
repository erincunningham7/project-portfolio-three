# Blackjack
## Index - Table Of Contents
1. [General Information](#general-info)
2. [User Experience & Design](#ux)
3. [Features](#features)
4. [Technologies Used](#tech-used)
5. [Testing](#testing)
6. [Deployment](#deployment)

<a name="general-info"></a>

## General Information

This is a simple blackjack game. This python game has all the attributes of the classic card game.  It uses decks of 52 cards, four suits, with the typical shuffle card technique, instructions and score board, this game envokes the quintessential casino game. The player plays against the computer/dealer with the strategy to beat the dealer's hand without going over 21.

<a name="ux"></a>

## User Experience

**Site Goals**

1. As A User
* I would like to be able to access the game instructions upon opening the game.
* I would like to be able to easily differentiate between card suits.
* I would like to have the option to take more cards if I wanted to.
* I would like to be able to see the dealer's first card, like in the classic blackjack game.
* I would like to be able to see the user score and computer score once the game is over.
* I would like the game to run smoothly and without errors.

2. As The Site Administrator
* I want the game to have simple, straightforward navigation.
* I want the game to be easy to use.
* I want the blackjack game to mimic all the characteristics of the classic game.

## Design

<a name="features"></a>

## Features

<a name="tech-used"></a>

## Technologies Used

**Languages Used**

**Frameworks, Libraries & Programs Used**

<a name="testing"></a>

## Testing

**Functional Testing**

*Card Class*

* Testing was ran on the card class to ensure it does it's intended task - creates the suits and ranks, implements the suit symbols and assigns the cards to their number value. This was assessed by creating two card variables and assigning each a specific rank and suit. The cards were then printed using the print statement. To test the return card value function, I assigned each card the function using dot notation and printed them.

* The card class worked as intended.

*Hand Class*

* Testing was carried out on the hand class to make sure the functions work in the correct fashion - give cards to each player, empty the deck at the beginning of each game and return the total value of cards in a players hand. To test, I assigned a my_hand variable to the hand class. Using dot notation I added both test cards to the newly created hand variable. Using print, I checked the terminal to see that both cards were now present in the hand. Afterwards I made a new variable to test the hand_total function, assigning it the my_hand variable and the hand_total() function using dot notation.

* The hand class worked as intended.

*Deck Class*

* Testing was done on the deck class to ensure it was working perfectly - creating a full deck of playing cards, looping through the suits and ranks and creating cards accordingly, shuffling the cards and lastly dealing the cards in the appropriate fashion. I created a deck variable and assigned it the deck class. The variable accessed the create_deck method using dot notation and was printed to the terminal. To test the shuffle function I used dot notation again to ingress the shuffle method, and used the print statement.

* The deck class worked as intended.

*Rules.txt*

* Testing was carried out on the rules text file to ensure the game rules were accessible to the player. This was done by calling the show_rules method.

* The rules.txt file worked as intended.

<a name="deployment"></a>

## Deployment

**Version Control**

The site was created using the Code Anywhere code editor and pushed to github to the remote repository "project-portfolio-three".

The following git commands were used throughout development to push code to the remote repo:

git status - This command was used to check which files were modified.

git add . - This command was used to add the changed files to the staging area before they are committed.

git commit -m "commit message" - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to push all committed code to the remote repository on github.

touch - This command was used to create new files.

