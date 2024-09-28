
import random
'''
Blackjack is a popular card game where players try to beat the dealer 
by having a hand value as close to 21 as possible without exceeding it.
Each card has a value: numbered cards are worth their face value, 
face cards (King, Queen, Jack) are worth 10, and Aces can be worth 1 or 11.

Players are dealt two cards and can choose to "hit" (take more cards) or "stand" (keep their current hand). 
The dealer follows set rules, typically hitting until their hand totals 17 or more. 
The goal is to have a hand higher than the dealer's without going over 21.
'''

cards = [10,10,10,10,9,8,7,6,5,4,3,2,11]

game_on_off = input("Do you want to play a game of BlackJack? Type 'y' or 'no':  ").lower()

your_cards = random.choices(cards, k=2)

current_score = sum(your_cards)

computers_card = random.choice(cards)

print(f"Your cards: {your_cards}, current score: {current_score}")
print(f"Computer's first card: {computers_card}")

hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")