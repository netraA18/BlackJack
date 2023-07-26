# pylint: disable-all
import random
import math

ranks = ['Ace', '2', '3', '4', '5', '6', '7',
         '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

deck = [(rank, "of", suit) for rank in ranks for suit in suits]

random.shuffle(deck)

players = str(input("How many players? "))
total = int(players) + 1 #Total players including the dealer


def ask_bet():
    total_bet = []
    numb_player = 1
    while numb_player <= int(players):
        bet_amount = str(input("Player " + str(numb_player) + ", " + "how much do you want to bet?: "))
        bet_amount = float(bet_amount)
        total_bet.append(bet_amount)
        numb_player += 1
    Sum = math.fsum(total_bet)
    Sum = int(Sum)
    print("The total bet in the middle is " + "$ " + str(Sum))


ask_bet()


def game():
    i = 0
    numb_player = 1
    store_results = []
    store_dealer = []
    while i < total: 
        deck_card = random.choice(deck) #for Deck 1
        deck_card2 = random.choice(deck) #for Deck 2
        get_numb = (deck_card)[0]
        get_numb2 = (deck_card2)[0]
        if i == 0:
            print("Dealer's 1st card: " + str(deck_card) + " Second Card: " + " face down ")
            second_cardd = (deck_card2)[0]
            if "Jack" in deck_card or "Queen" in deck_card or "King" in deck_card:
                store_dealer.append(10)
                
            if "Ace" in deck_card:
                ask_value = str(input("1 or 11?"))
                store_dealer.append(ask_value)
                
            if "Jack" not in deck_card and "Queen" not in deck_card and "King" not in deck_card and "Ace" not in deck_card:
                store_dealer.append(get_numb)
                
            if "Jack" in deck_card2 or "Queen" in deck_card2 or "King" in deck_card2:
                store_dealer.append(10)
                
            if "Ace" in deck_card2:
                ask_value = str(input("1 or 11?"))
                store_dealer.append(ask_value)
                
            if "Jack" not in deck_card2 and "Queen" not in deck_card2 and "King" not in deck_card2 and "Ace" not in deck_card2:
                store_dealer.append(get_numb2)
                
            print(store_dealer[0])
                     
        elif i > 0:
            print("Player " + str(numb_player) + ": " + str(deck_card) + " " + str(deck_card2))
            jqk_in_card1 = "Jack" in deck_card or "Queen" in deck_card or "King" in deck_card
            jqk_in_card2 = "Jack" in deck_card2 or "Queen" in deck_card2 or "King" in deck_card2
            jqk_not_card1 = "Jack" not in deck_card and "Queen" not in deck_card and "King" not in deck_card and "Ace" not in deck_card
            jqk_not_card2 = "Jack" not in deck_card2 and "Queen" not in deck_card2 and "King" not in deck_card2 and "Ace" not in deck_card2
            ace_card1 = "Ace" in deck_card
            ace_card2 = "Ace" in deck_card2
            
            if jqk_in_card1 or jqk_in_card2:
                if jqk_in_card1 and jqk_in_card2:
                    print("20")
                    store_results.append(20)
                    
            if ace_card1 or ace_card2:
                if ace_card1 and ace_card2:
                    ask_value = float(input("1 or 11? "))
                    ask_value2 = float(input("1 or 11? "))
                    result = ask_value + ask_value2
                    store_results.append(result)
                    print(result)
                    
                else:
                    ask_value3 = str(input("1 or 11? "))
                    
            if jqk_not_card1 or jqk_not_card2:
                if jqk_not_card1 and jqk_not_card2:
                    result = float(get_numb) + float(get_numb2)
                    print(int(result))
                    store_results.append(result)
                    
            if jqk_in_card1 and ace_card2 or jqk_in_card2 and ace_card1:
                get_value = float(ask_value3)
                result = get_value + float(10)
                print(int(result))
                store_results.append(result)

            elif jqk_not_card1 and ace_card2:
                get_value = float(ask_value3)
                result = float(get_numb) + get_value
                print(int(result))
                
                store_results.append(result)
            elif jqk_not_card2 and ace_card1:
                get_value = float(ask_value3)
                result = float(get_numb2) + get_value
                print(int(result))
                store_results.append(result)

            if jqk_in_card1 and jqk_not_card2:
                result = float(10) + float(get_numb2)
                print(int(result))
                store_results.append(result)
                
            elif jqk_in_card2 and jqk_not_card1:
                result = float(10) + float(get_numb)
                print(int(result))
                store_results.append(result)
            numb_player += 1
    
        i += 1
    print(store_results)
    
   
    numb_player = 1
    store_final = []
    while numb_player <= int(players):
        dict = {"in": 10}
        deck_card = random.choice(deck)
        ask_user = str(input("Player " + str(numb_player) + ", " + "hit or stand: "))
        if ask_user == "hit":
            print("here: " + str(deck_card))
            jqk_in_card1 = "Jack" in deck_card or "Queen" in deck_card or "King" in deck_card
            ace_card1 = "Ace" in deck_card
            if jqk_in_card1:
                access = dict["in"]
                results = float(access) + store_results[numb_player - 1]
                print(int(results))
                store_final.append(results)
                
            if ace_card1:
                ask_ace = str(input("1 or 11? "))
                results = float(ask_ace) + store_results[numb_player - 1]
                print(int(results))  
                store_final.append(results) 
                
            if not(jqk_in_card1) and not(ace_card1):
                get_numbber = (deck_card)[0]
                results = float(get_numbber) + store_results[numb_player - 1]
                print(int(results))  
                store_final.append(results)  
        else: 
            print(store_results[numb_player - 1])  
            store_final.append(store_results[numb_player - 1])   
        numb_player +=1
    print(store_final)
    
    numb_player = 1
    while numb_player <= int(players):
        compare1 = int(store_dealer[0]) + int(store_dealer[1])
        # print(compare1)
        if store_final[numb_player - 1] > float(compare1):
            print("Player " + str(numb_player) + " you lost")
        else:
            print("Player " + str(numb_player) + " you won")
        numb_player +=1
game()
