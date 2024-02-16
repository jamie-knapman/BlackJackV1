# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:45:47 2024

@author: jamie
"""
import random 

balance = 10000
quit_game = False
suits = ["Hearts","Diamonds","Clubs","Spades"]
vals = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "King": 10, "Queen": 10, "Jack": 10,
    "Ace": 11}   
class BlackJack:
    
    def __init__(self):
        BlackJack.initialise()
        
    def deal():
        global suits, vals
        suit = suits[random.randint(0,3)]
        val = random.choice(list(vals.keys()))
        return val, suit 
    
    def get_total(hand):
        total = sum(vals[card[0]] for card in hand)
        while total > 21 and any(card[0] == 11 for card in hand):
            total -= 10
        return total
        
    @staticmethod
    def play():
        global balance
        #input checking
        valid = False
        while valid == False:
            bet = int(input("Enter bet: "))
            if bet < balance:
                valid = True
                
        dealer_hand = [BlackJack.deal(), BlackJack.deal()]
        dealer_total = BlackJack.get_total(dealer_hand)
        player_hand = [BlackJack.deal(), BlackJack.deal()]
        player_total = BlackJack.get_total(player_hand)
        playing = True
        while playing:
            print("======================")
            print("Dealers Hand")
            print(dealer_hand)
            print(dealer_total)
            print("----------------------")
            print("Your Hand")
            print(player_hand)
            print(player_total)
            print("======================")
            print("Options")
            print("A - Hit")
            print("B - Stand")
            choice = str(input("").upper())
            if choice == "A":
                player_hand.append(BlackJack.deal())
                player_total = BlackJack.get_total(player_hand)
            elif choice == "B":
                while dealer_total < 17:
                    dealer_hand.append(BlackJack.deal())
                    dealer_total = BlackJack.get_total(dealer_hand)
                if dealer_total > 21:
                    print("The dealer has gone bust you win! \n \n \n")
                elif dealer_total > player_total:
                    print("The dealer has" + str(dealer_total) + " you lose!")
                elif player_total > dealer_total:
                    print("You win")
                playing = False
            if player_total > 21:
                playing = False
                print("You have gone bust! \n \n \n")
                balance -= bet
                
                
                
        
        
    @staticmethod
    def initialise():
        global balance, quit_game
        while not quit_game:
            print("Welcome to Blackjack \n" )
            print("Main menu. Select an option: ")
            print("Chips to play with: " + str(balance))
            print("A - Request more chips")
            print("B - Play!")
            print("C - Rules")
            print("D - Quit")
            
            option = str(input("").upper())
            if option == "A":
                balance += 1000
            elif option == "B":
                BlackJack.play()
            elif option == "C":
                pass
            elif option == "D":
                quit_game = True
            else:
                print("Invalid option")

blackjack = BlackJack()

        