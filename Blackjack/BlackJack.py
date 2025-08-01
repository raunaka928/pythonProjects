import art_Blackjack
import random

def calculate_hand(hand):
    total_value = sum(hand)
    if 11 in hand:
        if total_value > 21:
            ind = hand.index(11)
            hand[ind] = 1
            return calculate_hand(hand)
        else:
            return total_value
    else:
        return total_value

def stand(comp_hand):
    total_comp_hand = calculate_hand(comp_hand)
    if total_comp_hand <= 16:
        comp_hand.append(random.choice(cards))
        stand(comp_hand)
        return comp_hand
    elif total_comp_hand >= 17:
        return comp_hand
def prints(x):
    if x == 1:
        print(f"Your cards are {players_cards}, current score: {player_hand}")
        print(f"Computer's First Card: {dealers_cards[0]}")
    elif x == 2:
        print(f"Your final cards are {players_cards}, Final score: {player_hand}")
        print(f"Computer's Final cards: {dealers_cards}, Final score: {dealer_hand}")
    elif x ==3:
        print(f"Your final cards are {players_cards}, Final score: {player_hand}")
        print(f"Computer's First Card: {dealers_cards[0]}")
# def check_winner(comp,player):
#     if calculate_hand(player)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on = True
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while game_on:
    players_cards = []
    dealers_cards = []
    if play == "y":
        print(art.logo)
        players_cards = random.choices(population=cards,k=2)
        dealers_cards = random.choices(population=cards, k=2)
        cont_play = True
        while cont_play:
            player_hand = calculate_hand(players_cards)
            dealer_hand = calculate_hand(dealers_cards)
            prints(1)
            if player_hand == 21 and dealer_hand != 21:
                prints(2)
                print("You Win")
                cont_play = False
                continue
            next_play = input("Type 'y' to hit and 'n' to stand: ")
            if next_play == 'y':
                players_cards.append(random.choice(cards))
                player_hand = calculate_hand(players_cards)
                if player_hand > 21:
                    cont_play = False
                    prints(2)
                    print("You went over. You lose")
            elif next_play == 'n':
                dealer_cards = stand(dealers_cards)
                dealer_hand = calculate_hand(dealer_cards)
                prints(2)
                if dealer_hand > 21:
                    cont_play = False
                    print("Opponent went Over. You win!")
                elif dealer_hand < 21:
                    if dealer_hand < player_hand:
                        cont_play = False
                        print("You Win")
                    elif dealer_hand > player_hand:
                        cont_play = False
                        print("You lose")
                    elif dealer_hand == player_hand:
                        cont_play = False
                        print("Draw")
                elif dealer_hand == 21:
                    if player_hand == 21:
                        print("Draw")
                        cont_play = False
                    else:
                        print("Opponent has Blackjack. You lose")
                        cont_play = False

    new_game = input("Do you want to play another game? Type 'y' or 'n'")
    if new_game == 'n':
        game_on = False
    elif new_game == 'y':
        play = 'y'
        print("\n"*20)
        continue














