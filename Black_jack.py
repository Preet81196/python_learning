import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = []
        for i in range(num_cards):
            dealt_cards.append(self.cards.pop())
        return dealt_cards

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_cards = []
        self.dealer_cards = []
        self.player_points = 0
        self.dealer_points = 0
        self.game_over = False

    def start(self):
        print("Welcome to Blackjack!")
        print("Dealing cards...")
        self.player_cards = self.deck.deal(2)
        self.dealer_cards = self.deck.deal(2)
        self.player_points = self.calculate_points(self.player_cards)
        self.dealer_points = self.calculate_points(self.dealer_cards)
        self.display_cards()

        while not self.game_over:
            self.player_turn()
            if self.game_over:
                break
            self.dealer_turn()
            self.determine_winner()
            self.play_again()
            
    def player_turn(self):
        while True:
            choice = input("Would you like to hit or stay? (h/s) ")
            if choice == "h":
                self.player_cards.append(self.deck.deal(1)[0])
                self.player_points = self.calculate_points(self.player_cards)
                self.display_cards()
                if self.player_points > 21:
                    print("You have lost the game.")
                    self.game_over = True
                    break
                elif self.player_points == 21:
                    print("You have won the game.")
                    self.game_over = True
                    break
            elif choice == "s":
                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

    def dealer_turn(self):
        while self.dealer_points < 16:
            self.dealer_cards.append(self.deck.deal(1)[0])
            self.dealer_points = self.calculate_points(self.dealer_cards)

    def determine_winner(self):
        if self.player_points > 21:
            print
