import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
            
            
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f'The card is {self.rank} of {self.suit}'
        
        
class Deck:
    
    def __init__(self):
        self.all_cards = list()
    
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def mix(self):
        random.shuffle(self.all_cards)
        
    def last_card(self):
        self.card = self.all_cards.pop()
        return self.card
    
    def __str__(self):
        buf = list()
        for card in self.all_cards:
            buf.append(f'The card is {card.rank} of {card.suit}')
        return str(buf)
        
        
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        
    def adjust_for_ace(self, card):
        
        if card.rank == 'Ace':
            self.aces += 1
    
    def calculate(self):
        
        self.value = 0
        for card in self.cards:
            
            if card.rank == 'Ace':
                if self.value <= 21:
                    self.value += 11
                else:
                    self.value += 1
            else:
                self.value += card.value
    
    def __str__(self):
        return str(self.cards)
        
        
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet*2
    
    def lose_bet(self):
        self.total -= self.bet 
        
    def __str__(self):
        return f'Your balance is ${self.total}. Your last bet was ${self.bet}'
        
 
def take_bet(chips):
    
    x = 0
    while True:
        try:
            x = int(input('Place your bet: '))
            
        except TypeError:
            print('Please, enter the number: ')
        except ValueError:
            print('Please, enter the number: ')
            
        else:
            if int(x) > chips.total:
                print("You don't have that much money!")
                continue
            else:
                chips.bet = int(x)
                break

def hit(deck,hand):
    
    x = deck.last_card()
    hand.add_card(x)
    
    if x.rank == 'Ace':
        hand.adjust_for_ace(x)
        
        
def hit_or_stand(deck,hand):
    
    ques = input('\nDo you hit or stand? ')
    
    global playing # to control an upcoming while loop
    
    if ques.upper() == 'HIT':
        playing = True
        hit(deck, hand)
        
        return playing
        
    if ques.upper() == 'STAND':
        playing = False
        
        return playing
        
        
def show_some(player,dealer):
    
    print('These are player`s cards: ')
    
    for i in player.cards:
        print(i)
        
    player.calculate()
    print(f'Value of player`s cards: {player.value}')
        
    print('These are dealer`s cards: ')
    
    for d in range(len(dealer.cards) - 1):
        print(dealer.cards[d])

def show_all(player,dealer):
    
    print('Player`s cards: ')
    
    player_value = 0
    for i in player.cards:
        player_value += i.value
        print(i)
        
    print(f'Value of player`s cards: {player_value}\n')
    
    print('Dealer`s cards: ')
    
    dealer_value = 0
    for d in dealer.cards:
        dealer_value += d.value
        print(d)
        
    print(f'Value of dealer`s cards: {dealer_value}\n')


def ask_for_game():
    
    x = input('Do you want to play again? ')
    
    if x.upper() == 'YES':
        return True
    else:
        print('See you next time!')
        return False
        

def player_busts(player, dealer, chips):
    
    print('\nPlayer has lost!\n')
    
    chips.lose_bet()   
    show_all(player, dealer)
    
    player.cards = []
    dealer.cards = []
    
    print(chips)
    
def player_wins(player, dealer, chips):
    
    print('\nPlayer has won!\n')
    
    chips.win_bet()
    show_all(player, dealer)
    
    player.cards = []
    dealer.cards = []

    print(chips)
    
def dealer_busts(player, dealer, chips):
    
    print('\nDealer busted! Player has won!')
    
    chips.win_bet()
    show_all(player, dealer)
    
    player.cards = []
    dealer.cards = []
    
    print(chips)
    
def push(player, dealer, chips):
    
    print('\nIt`s draw!\n')
    
    show_all(player, dealer)
    
    player.cards = []
    dealer.cards = []
    
    print(chips)
    
    
# Set up the Player's chips
player_chips = Chips()
from IPython.display import clear_output

while True:
    # Print an opening statement
    print('Hello! Welcome to BlackJack game!')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.mix()
    
    player = Hand()
    dealer = Hand()
    
    for i in range(2):
        x = deck.last_card()
        player.add_card(x)
        player.adjust_for_ace(x)
        y = deck.last_card()
        dealer.add_card(y)
        dealer.adjust_for_ace(y)
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)
    
    playing = True
    
    flag = 0
    
    while playing == True:
        
        hit_or_stand(deck, player)
        
        show_some(player, dealer)
        
        if player.value > 21:
            player_busts(player, dealer, player_chips)
            flag = 1
            break
        if player.value == 21:
            player_wins(player, dealer, player_chips)
            flag = 1
            break
                    
    while True and flag != 1:
        dealer.calculate()
        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)
            flag = 1
            break
        if dealer.value <= 17:
            hit(deck, dealer)
        else:
            break 
    
    if flag == 0:
        if player.value > dealer.value:
            player_wins(player, dealer, player_chips)
        elif player.value < dealer.value:
            player_busts(player, dealer, player_chips)
        else:
            push(player, dealer, player_chips)
    
    if ask_for_game() == True:
        clear_output(wait=True)
        continue
    else:
        break    
