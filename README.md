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

*Play Game Function*

* This function was tested to verify it was running effectively - allowing the user to play the card game against the computer, flagging the end of the game, creating hands for both the player and the computer, dealing cards to the player and the computer, getting player and computer hand totals, adding inputs for the user to take or refuse a card, ending the game if the card hand total is over 21 and creating the computers moves. 

To test it's functionality, I began with the blackjack_deck variable accessing the deal method using dot notation, and passing in the recently created players variable and the number 2 as arguments in the parentheses. By printing the player hand and the computer hand variables, I could easily analyse the code result in the terminal.

I had to check the player score's and computer score's viability. I created variables of the same name and assigned them to the player/computer hand, which were then appeneded to the hand total function. I subsequently printed both player and computer score variables.

![Image](images/test-score.png)

The first while loop had to be assessed too. To achieve this I printed the player hand and player score and the same for the computer hand and score.

When the final while loop was done and the entirety of the function was completed I did the final analysis. I repeated the print steps for the previous while loop.






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

**Heroku Deployment**

To deploy the project to Heroku the following steps were implemented:

1. Log in to Heroku and click "New" to create a new app.
2. Choose an app name and region, then click "Create app".
3. Go to "Settings" and navigate to Config Vars. Add PORT 8000.
4. Navigate to Buildpacks and add buildpacks for Python and NodeJS, ensuring they are strictly in that order.
5. Navigate to the "Deploy" section. Set the deployment method to Github and enter the chosen repository name and then connect.
6. Scroll down the page, click Automatic Deploy, select "main" branch and click "Deploy Branch".
7. The app will now be deployed to heroku.


