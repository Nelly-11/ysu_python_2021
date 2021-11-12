"""
lecture 6 homework
"""

from abc import ABC, abstractmethod
from itertools import product
from random import shuffle
from time import sleep


class CardABC(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def value(self):
        pass


class DeckABC(ABC):

    @abstractmethod
    def create_deck(self):
        pass

    @abstractmethod
    def shuffle(self, deck):
        pass


class Card(CardABC):
    # suits = {"spades", "diamonds", "clubs", "hearts"}
    suits = {"♠", "♦", "♣", "♥"}
    ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}

    def __init__(self, suit, rank):
        if suit in self.__class__.suits:
            self.suit = suit
        else:
            raise LookupError("Suit not found")

        if rank in self.__class__.ranks:
            self.rank = rank
        else:
            raise LookupError("Card initiation failed: check the card rank")
        self.soft, self.hard = self.value()

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        return None, None


class FaceCard(Card):
    ranks = {"J", "Q", "K"}

    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):
        return 10, 10


class AceCard(Card):
    ranks = {"A"}

    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):
        return 1, 11


class NumCard(Card):
    ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10"}

    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):
        return int(self.rank), int(self.rank)


class Deck(DeckABC):

    def __init__(self):
        self.deck = Deck.create_deck(self)
        Deck.shuffle(self, deck_=self.deck)

    def __len__(self):
        return self.deck.__len__()

    def deal(self):
        return self.deck.pop()

    def create_deck(self):
        variants = \
            list(product([FaceCard], FaceCard.suits, FaceCard.ranks)) + \
            list(product([AceCard], AceCard.suits, AceCard.ranks)) + \
            list(product([NumCard], NumCard.suits, NumCard.ranks))

        _deck = []
        for class_, suit, rank in variants:
            _deck.append(class_(suit, rank))
        return _deck

    @staticmethod
    def shuffle(self, deck_):
        shuffle(deck_)


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win = None
        self.soft = None
        self.hard = None

    def __repr__(self):
        represent = self.name + ": | "

        for card in self.hand:
            if card[1]:
                represent += card[0].__repr__() + " | "
            else:
                represent += "<card hidden>" + " | "

        return represent


class Game:

    def __init__(self, deck):
        print("Welcome to Blackjack!")
        self.deck = deck
        self.number_of_players = 1
        self.max_players = 6
        self.dealer = Player("Dealer")
        self.users = []
        Game.add_player(self)
        Game.initial_deal(self)
        Game.show_status(self)

    @staticmethod
    def add_player(self):
        if self.number_of_players < self.max_players:
            ask_player = input("Do you want to add a player (y/n):")
            if ask_player == "y":
                name = input("Please enter the player's name: ")
                self.users.append(Player(name=name))
                print(f"{name} added!")
                self.number_of_players += 1
                Game.add_player(self)
            elif ask_player == "n":
                pass
            else:
                print("Please enter 'y' or 'n'")
                Game.add_player(self)
        else:
            print("You reached maximum number of players!")
        if self.number_of_players == 1:
            print("No player joined the game")
            quit() # TODO

    @staticmethod
    def initial_deal(self):
        print("__________________________")
        print("Starting the game")
        sleep(1)
        for player in [self.dealer] + self.users:
            player.hand.append((self.deck.deal(), True))
        self.dealer.hand.append([self.deck.deal(), False])
        for player in self.users:
            player.hand.append((self.deck.deal(), True))

    def show_status(self):
        for player in [self.dealer] + self.users:
            print(player)

    @staticmethod
    def check_hand(self, hand):
        soft_sum, hard_sum = 0, 0
        for card in hand:
            soft_sum += card[0].soft
            hard_sum += card[0].hard
        return soft_sum, hard_sum

    def ask_user(self, user: Player):
        print("__________________________")
        print(f"Playing with {user.name}")

        def looping():
            soft_sum, hard_sum = Game.check_hand(self, user.hand)
            print(user)
            if soft_sum == hard_sum:
                print(f"Your total is {soft_sum}")
            else:
                print(f"Your sums are - soft: {soft_sum}, hard: {hard_sum}")

            if soft_sum == 21 or hard_sum == 21:
                print("Blackjack!!! You won")
                user.win = 1
                return None
            if soft_sum > 21:
                print("You bust (((")
                user.win = 0
                return None
            ask_player = input("Do you want another card (y/n):")
            if ask_player == "y":
                user.hand.append((self.deck.deal(), True))
                looping()
            elif ask_player == "n":
                user.soft, user.hard = soft_sum, hard_sum
            else:
                print("Please enter 'y' or 'n'")
                looping()

        looping()

    def ask_dealer(self):

        print("__________________________")
        print(f"Dealer showing")
        self.dealer.hand[1][1] = True

        def looping():
            soft_sum, _ = Game.check_hand(self, self.dealer.hand)
            print(self.dealer)

            print(f"Dealer's total is {soft_sum}")

            if soft_sum<=16:
                print("Opening a card")
                self.dealer.hand.append((self.deck.deal(), True))
                looping()
                sleep(1)
            else:
                self.dealer.soft = soft_sum
                if self.dealer.soft>=21:
                    print("Dealer bust (((")
                    self.dealer.win = 0

        looping()

        print("__________________________")
        print("Final Results are:")
        for player in self.users:
            if player.win == 0:
                print(f"\tPlayer {player.name} LOST(((")
            elif player.win == 1 or self.dealer.win == 0:
                player.win = 1
                self.dealer.win = 0
                print(f"\tPlayer {player.name} WIN!")
            else:
                if player.soft > self.dealer.soft or player.hard > self.dealer.soft:
                    player.win = 1
                    print(f"\tPlayer {player.name} WON!")
                else:
                    player.win = 0
                    print(f"\tPlayer {player.name} LOST(((")
        print("__________________________")

    @staticmethod
    def start_again():
        answer = input("Do you want to start again (y/n)?")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please answer")
            Game.start_again()


def main():
    def looping():
        deck = Deck()
        game = Game(deck)
        for user in game.users:
            game.ask_user(user=user)
        game.show_status()
        game.ask_dealer()
        if game.start_again():
            looping()
    looping()
    print("Thanks. Bye!")


if __name__ == "__main__":
    main()
