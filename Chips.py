class Chip:

    def __init__(self,total=500):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self, chip):
        while True:
            try:
                chip.bet = int(input('Сделайте вашу ставку'))

            except:
                print('Вводить можно только числа')
            else:

                if chip.bet > chip.total:
                    print(f'Извините у вас недостаточно фишек. У вас {chip.total} фишек')
                else:
                    break

