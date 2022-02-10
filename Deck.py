import random


class Deck:

    def __init__(self):
        self.shuffle_deck = []

    def generate_deck(self):
        deck = []
        for y in range(4):
            x = 0.5
            value = []
            for i in range(13):
                suit = []
                x += 0.5
                for j in range(2):
                    suit.append(0)
                    suit[0] += x
                value.append(suit)
                suit[1] += y
            deck.append(value)

        j = 0
        for i in range(len(deck)):
            for j in range(len(value)):
                self.shuffle_deck.append(deck[i][j])
            j += 1
        random.shuffle(self.shuffle_deck)
        return self.shuffle_deck
