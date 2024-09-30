
import random
from art import card_logo, blackjack
'''
Blackjack is a popular card game where players try to beat the dealer 
by having a hand value as close to 21 as possible without exceeding it.
Each card has a value: numbered cards are worth their face value, 
face cards (King, Queen, Jack) are worth 10, and Aces can be worth 1 or 11.

Players are dealt two cards and can choose to "hit" (take more cards) or "stand" (keep their current hand). 
The dealer follows set rules, typically hitting until their hand totals 16 or more. 
The goal is to have a hand higher than the dealer's without going over 21.
'''

cards = [10,10,10,10,9,8,7,6,5,4,3,2,11]

print(card_logo)
print(blackjack)
print('\n' * 5)

keep_playing = True

def greeting():
    game_on_off = input("Let's start the game. Type 'y' or 'n':  ").lower()
    print('\n')
    return game_on_off

while keep_playing:
    your_cards = random.choices(cards, k=2)
    computers_cards= random.choices(cards, k=2)

    while sum(computers_cards) < 16:
        computers_cards.append(random.choice(cards))


    print(f"    Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"    Computer's first card: {computers_cards[0]}")

    should_continue = True

    def get_result():
        if sum(your_cards) == [10, 11] or sum(your_cards) == [11, 10]:
            print("You win. 🎉 BLACKJACK 🎉 \n")
        elif sum(computers_cards) == [10, 11] or sum(computers_cards) == [11, 10]:
            print("You win. Opponent has 🎉 BLACKJACK 🎉 \n")
        elif sum(computers_cards) > 21 and sum(your_cards):
            print("Oh no! You both have gone over 21 😱")
        elif sum(your_cards) > sum(computers_cards) and sum(your_cards) < 22:
            print("You win 🥳 \n")
        elif sum(your_cards) < sum(computers_cards) and sum(computers_cards) < 22:
            print("You lose 😢 \n")
        elif sum(your_cards) < sum(computers_cards) and sum(computers_cards) > 21:
            print("You win 🥳 Opponent has gone over 21. \n")
        elif sum(your_cards) > sum(computers_cards) and sum(your_cards) > 21:
            print("You lose 😢 You have gone over 21. \n")
        elif sum(your_cards) == sum(computers_cards) and sum(computers_cards) < 22 and sum(your_cards) < 22:
            print("draw 🤪")
        
        

    def get_final_message():
        print(f"    Your final hand: {your_cards}, final score: {sum(your_cards)}")
        print(f"    Computer's final hand: {computers_cards}, final score: {sum(computers_cards)}")
        print('\n')
        get_result()

    while should_continue:
        hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit_or_stand == 'y':
            new_card = random.choice(cards)
            your_cards.append(new_card)
            sum(your_cards)
            print(f"    Your cards: {your_cards}, current score: {sum(your_cards)}")
            print('\n')
            if sum(your_cards) > 21:
                # print(f"    Your final hand: {your_cards}, final score: {sum(your_cards)}")
                # print(f"    Computer's final hand: {computers_cards}, final score: {sum(computers_cards)}")
                # print('\n')
                # get_result()
                get_final_message()
                should_continue = False
                
        elif hit_or_stand == 'n' and sum(your_cards) < 16:
            print(" Sorry, you haven't reached total 16, you have to get more cards \n")
        else: 
            # print(f"    Your final hand: {your_cards}, final score: {sum(your_cards)}")
            # print(f"    Computer's final hand: {computers_cards}, final score: {sum(computers_cards)}")
            # print('\n')
            # get_result()
            get_final_message()
            should_continue = False

    if greeting() == 'n':
        keep_playing = False