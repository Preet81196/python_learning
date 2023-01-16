import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

deck = Deck()
deck.shuffle()
print(f"Total number of cards in the deck: {len(deck.cards)}")

player_hand = [deck.deal(), deck.deal()]
dealer_hand = [deck.deal(), deck.deal()]

while True:
    player_points = sum(card.rank for card in player_hand)
    print(f"Player's hand: {player_hand}, total points: {player_points}")
    if player_points > 21:
        print("Player loses!")
        break
    elif player_points == 21:
        print("Player wins!")
        break

    choice = input("Do you want another card? (y/n)")
    if choice == "y":
        player_hand.append(deck.deal())
    else:
        break

while True:
    dealer_points = sum(card.rank for card in dealer_hand)
    print(f"Dealer's hand: {dealer_hand}, total points: {dealer_points}")
    if dealer_points > 21:
        print("Dealer loses!")
        break
    elif dealer_points >= 16:
        if dealer_points > player_points:
            print("Dealer wins!")
        elif dealer_points < player_points:
            print("Player wins!")
        else:
            print("Tie!")
        break
    else:
        dealer_hand.append(deck.deal())
        
play_again = input("Do you want to play again? (y/n)")
if play_again == "y":
    continue
else:
    break
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

deck = Deck()
deck.shuffle()
print(f"Total number of cards in the deck: {len(deck.cards)}")

player_hand = [deck.deal(), deck.deal()]
dealer_hand = [deck.deal(), deck.deal()]

while True:
    player_points = sum(card.rank for card in player_hand)
    print(f"Player's hand: {player_hand}, total points: {player_points}")
    if player_points > 21:
        print("Player loses!")
        break
    elif player_points == 21:
        print("Player wins!")
        break

    choice = input("Do you want another card? (y/n)")
    if choice == "y":
        player_hand.append(deck.deal())
    else:
        break

while True:
    dealer_points = sum(card.rank for card in dealer_hand)
    print(f"Dealer's hand: {dealer_hand}, total points: {dealer_points}")
    if dealer_points > 21:
        print("Dealer loses!")
        break
    elif dealer_points >= 16:
        if dealer_points > player_points:
            print("Dealer wins!")
        elif dealer_points < player_points:
            print("Player wins!")
        else:
            print("Tie!")
        break
    else:
        dealer_hand.append(deck.deal())
        
play_again = input("Do you want to play again? (y/n)")
if play_again == "y":
    continue
else:
    break
