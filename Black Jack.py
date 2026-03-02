import random

# setting values of global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks =(
     "Two",
     "Three",
     "Four",
     "Five",
     "Six",
     "Seven",
     "Eight",
     "Nine",
     "Ten",
     "Jack",
     "Queen",
     "King",
     "Ace",
)
values = {
     "Two":2,
     "Three":3,
     "Four":4,
     "Five":5,
     "Six":6,
     "Seven":7,
     "Eight":8,
     "Nine":9,
     "Ten":10,
     "Jack":10,
     "Queen":10,
     "King":10,
     "Ace":11,
   }
chips = 100
game_num = 0
game_on = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
        
class Deck:
    """
    A class representing a deck of playing cards.

    The Deck class manages a collection of Card objects, providing functionality
    to initialize a standard deck, shuffle it, and deal cards one at a time.

    Attributes:
        deck (list): A list of Card objects representing all cards in the deck.

    Methods:
        __init__(): Initializes a full deck with all combinations of suits and ranks.
        shuffle(): Randomly shuffles the order of cards in the deck.
        deal_one(): Removes and returns the top card from the deck.
    """
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Cards class has already have been defined! 
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        # we remove one card from the list of all_cards
        return self.deck.pop()     


def check_ace(card):
    """
    fucntion to check for ace and adjust its value according to the user
    """
    if card.rank == "Ace":
        while True:
            ace_val = int(
                input("\nWhat value do you want to consider for Ace (1/11)? :")
            )

            if ace_val == 1:
                values["Ace"] = 1 

                break
            elif ace_val == 11:
                values["Ace"] = 11
                break
            else:
                print("choose valid value.")
                continue
                
                print()
                """
                
                        
                ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
                ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
                ██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
                ██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
                ██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
                ╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"""
                      
                
                print (
                """
    "Black jack is very popular card game played in casinos around the world.
    Let's imagine this program as a virtual casino with computer as the Dealer.
    The Purpose of the game is to beat the dealer, which can be done in various ways.
                            
    -------------------------------------------------------------------------------------------------------------------------------------
    Both the player and the dealer are given 2 cards at the beginning , but one of the dealer's card is kept hidden. 

    Each card holds a certain value.
    Number cards contain value identical to their number.
    All face cards hold a value of 10
    Ace can either holds a value of 1 or 11 depending on the situation.

    Blacjack means 21.Whoever gets a total value of 21 with their cards immediately wins!
    (winning through blackjack results in 3x the money)
    If the value of cards goes over 21, it's called a BUST, which results in an immediate loss...
     If both the players get the same value of cards , it's a TIE and the bet money is returned.

    If none of the above cases are met ,the person with closer value to 21 wins.
    (winning like this returns 2x the bet money)

------------------------------------------------------------------------------------------------------------------------------------------------------
    ("Good luck and have fun! Enjoy responsibly!"))
        
    Let the game begin!"""
      )
                         
    while game_on:
        try:
            new_deck = Deck() #  new deck will be created and shuffled each round
            new_deck.shuffle()

            game_num +=1
            print(f"\n\nGame Number: {game_num}")
            print(f"Chips remaining ={chips}")

            while True:
                bet = int(input("\nEnter the amount of chips you want to bet:"))
                if bet > chips:
                    print("You don't have enough chips.")
                    print("Enter a valid amount. \n")
                elif bet <= 0:  # To prevent betting a negative value
                    print("Invalid Bet amount. \n")
                else:
                    chips -= bet
                
                    break
                
            player_table_cards = []   # cards on table will be replaced each round
            dealer_table_cards = []

            # using list comprehension to distribute 2 cards
            [player_table_cards.append(new_deck.deal_one()) for i in range(2)]
            # to both user and dealer(computer)
            [dealer_table_cards.append(new_deck.deal_one()) for i in range(2)]

            print(f"\nPlayer cards are {player_table_cards[0]} and {player_table_cards[1]}")
            print(f"Dealer cards are {dealer_table_cards[0]} and Hidden.")
             # checking both the cards given to the user for being ace 
            check_ace(player_table_cards[0])
            check_ace(player_table_cards[1])

            while True:
                hit_or_stand = input("Do you want to hit or stand? :").lower()

                if hit_or_stand ==  "hit":
                    player_table_cards.append(new_deck.deal_one())
                    check_ace(player_table_cards[-1])

                    print(f"\nplayer's hand :")
                    #using list comprehension to  print cards on table
                    [print(i) for i in player_table_cards]
                    print()

                    player_cards_val = 0

                    for i in player_table_cards:
                        player_cards_val += i.value

                    if player_cards_val > 21:
                        print("You got a bust!")
                        break

                    elif player_cards_val == 21: # looping the options again 
                        print("You got a blackjack!")
                        break
                    else:
                        continue

                elif hit_or_stand == "stand":
                    player_cards_val = 0
                    for i in player_table_cards:
                        player_cards_val += i.value

                    print("\nplayer has decided to stand.")

                    print("\nplayer's hand :")
                    [print(i) for i in player_table_cards]
                    print()

                    if player_cards_val == 21:
                        print("player got a blackjack!")

                    break 

                else:
                    print("Enter a valid option. \n")
                    continue
               
                
            # variable that stores how many times dealer hits before cards value more than equal to 17
            no_of_hits = 0

            while True:
                dealer_cards_val = 0
                                
                for i in dealer_table_cards: #updating value of dealer's cards
                    dealer_cards_val += i.value

                if dealer_cards_val < 17:
                    no_of_hits += 1
                    dealer_table_cards.append(new_deck.deal_one())
                    continue
                elif 17 <= dealer_cards_val < 21:
                    print(f"The dealer hits {no_of_hits} times.")
                    print("\ndealer's hand :")
                    [print(i) for i in dealer_table_cards]
                    break

                else:
                    break
                           
            # checking for busts first
            if player_cards_val > 21:
                print(
                    "\nSince the player busted , the round is lost.\nPlayer lost the bet money" 
                )
            elif dealer_cards_val > 21:
                print(
                    "\n Since the Dealer busted , Player won the round! \nPlayer got twice the money bet."
                 )
                chips += bet * 2

            # checking for player's blackjack then
            elif player_cards_val == 21:
                print("\nPlayer won with a blackjack! \nPlayer got thrice the money bet.")
                chips += bet * 3

            #checking whose value is closer to 21
            elif 21 - player_cards_val > 21 - dealer_cards_val:
                print("\nDealer wins the round. \nPlayer lost the bet money.")
                            
                            
            elif 21 - player_cards_val < 21 - dealer_cards_val:
                print("\nPlayer wins the round! \nPlayer got twice the money bet.")
                chips += bet * 2
                            
            # last situation can only be a tie
            else:
                print("\nIt's a tie! \nPlayer's bet money is returned.")
                chips += bet
                            
            if chips == 0:
                print("You have run out of chips! Game over.")
                break
                           
            else:
                cont = input("Do you want to continue? (y/n) :")
                check = cont.upper() ###So a capital or lowercase value can be entered
                                 
                                        
                           
            if check == "Y":
                print("\n" * 100)

                print(
                    """
                                            
                                            
                                            
                                            
                                      ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
                                      ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
                                      ██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
                                      ██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
                                      ██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
                                      ╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"""
                     )
                                     
                continue

            else:
                print(f"\nTotal amount of chips left = {chips}")
                print(input("Press Enter to exit the terminal..."))
                break
    
        except Exception as error:
            print(f"Following error occured: {error}  \nPlease try again.")
            game_num -= 1 # round with error won't be counted 
            
            continue
    