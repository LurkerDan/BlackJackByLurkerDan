class Hand:

    def __init__(self,current_deck):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.suit = ''
        self.current_deck = current_deck

    def __str__(self):
        if self.card[1] == 0:
            self.suit = '\u2660'
        elif self.card[1] == 1:
            self.suit = '\u2665'
        elif self.card[1] == 2:
            self.suit = '\u2663'
        else:
            self.suit = '\u2666'
        if self.card[0]<10:
            self.sing = ' ' + str(int(self.card[0]))
        elif self.card[0] == 10:
            self.sing = int(self.card[0])
        elif self.card[0] == 11:
            self.sing = ' J'
        elif self.card[0] == 12:
            self.sing = ' Q'
        elif self.card[0] == 13:
            self.sing = ' K'
        else:
            self.sing = ' A'

        return f'_______\n|{self.suit}  {self.sing}|\n|     |\n|     |\n|_____| \n'

    def add_card(self):

        self.card = self.current_deck.pop()
        self.cards.append(self.card)
        if self.card[0] == 14:
            self.aces += 1
            self.value += 11
        elif self.card[0] > 10:
            self.value += 10
        else:
            self.value += self.card[0]
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def print_value(self,name):
        print(f'Очки {name} = {int(self.value)}')


