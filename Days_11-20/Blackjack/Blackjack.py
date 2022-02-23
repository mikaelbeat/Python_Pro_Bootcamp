
import random
from Art import logo
from replit import clear


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

def deal_cards(deck, number_of_cards):
    starting_cards = random.choices(cards, k=number_of_cards)
    
    for card in starting_cards:
        if sum(deck) > 21 and card == 11:
            deck.append(1)
        else:
            deck.append(card)


def show_cards():
    print(f"Your cards: {player_cards} -> {sum(player_cards)}")
    print(f"Computer cards: {computer_cards} -> {sum(computer_cards)}") 
    
def another_card():
    new_card = input("Do you want another card, y or n? ")
    print("*****************************************")
    if new_card == "y":
        deal_cards(player_cards, 1)
        if sum(computer_cards) < 17:
            deal_cards(computer_cards, 1)
        return True
    elif new_card == "n":
        if sum(computer_cards) < 17:
            deal_cards(computer_cards, 1)
        return False

def declare_winner(player, computer):
    if computer > 21 and player > 21:
        return "Both loses!"
    elif player < 22 and player > computer:
        return "You win!"
    elif player > 21:
        return "You lose!"
    elif computer < 22 and computer > player:
        return "Computer wins!"
    elif computer > 21:
        return "Computer loses!"
    else:
        return "Draw!"
    

def blackjack():
    clear()
    print(logo)
    new_card = True
    
    deal_cards(player_cards, 2)
    deal_cards(computer_cards, 2)
    
    while sum(player_cards) < 22 and sum(computer_cards) < 22 and new_card:
        show_cards()
        new_card = another_card()
       
    print(f"Your final hand {(player_cards)} -> {sum(player_cards)}")
    print(f"Computer final hand: {computer_cards} -> {sum(computer_cards)}")
    print(declare_winner(sum(player_cards), sum(computer_cards)))
    
    
    new_game = input("Do you want a new game, y or n? ")
    if new_game == "y":
        player_cards.clear()
        computer_cards.clear()
        blackjack()
    else:
        print("Thanks for playing.")
    
blackjack()