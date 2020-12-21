import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    
    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'




player1 = Player('Robot 1')
player2 = Player('Robot 2')
new_deck = Deck()
new_deck.shuffle()


for card in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())


round_num = 0

game_on = True

while game_on:
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player1.all_cards) == 0:
        print(player1.name +' has lost')
        game_on = False
        break      
    if len(player2.all_cards) == 0:
        print(player2.name + " has lost")
        game_on = False
        break
    
    

    player1_hand = []
    player2_hand = []



    player1_hand.append(player1.remove_one())
    player2_hand.append(player2.remove_one())


    at_war = True

    if player1_hand[-1].value > player2_hand[-1].value:
        print(player1.name + " Wins!")
        player1.add_cards(player2_hand)
        player1.add_cards(player1_hand)
        at_war = False

    elif player1_hand[-1].value < player2_hand[-1].value:
        print(player2.name + " Wins!")
        player2.add_cards(player1_hand)
        player2.add_cards(player2_hand)
        at_war = False



    while at_war:
        if len(player1.all_cards) < 5:
            print(player1.name +' has lost')
            print(player1)
            print(player2)
            game_on = False
            break      
        if len(player2.all_cards) < 5:
            print(player2.name + " has lost")
            print(player1)
            print(player2)
            game_on = False
            break
        print(" AT WAR!!! ")
        for i in range(5):
            player1_hand.append(player1.remove_one())
        for i in range(5):
            player2_hand.append(player2.remove_one())



        if player1_hand[-1].value > player2_hand[-1].value:
            print(player1.name + " Wins!")
            player1.all_cards.extend(player2_hand)
            player1.all_cards.extend(player1_hand)
            at_war = False

        if player1_hand[-1].value < player2_hand[-1].value:
            print(player2.name + " Wins!")
            player2.all_cards.extend(player1_hand)
            player2.all_cards.extend(player2_hand)
            at_war = False
        break

