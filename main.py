from Hand import Hand
from Chips import Chip
from Deck import Deck
import time

chip = Chip()

deck = Deck()
current_deck = deck.generate_deck()

player = Hand(current_deck)
dealer = Hand(current_deck)

temp_dcard = ''
temp_pcard = ''



start_on = True

# Ставка

while start_on:
    start = input('Black Jack by LurkerDan \n Начать новую игру? Y or N').lower()

    if start == 'y':
        game_on = True

    else:
        print('Пока!')
        exit()
    print(f'Ваши фишки {chip.total}')
    chip.take_bet(chip)
    while game_on:
        # Обнуление
        current_deck = deck.generate_deck()
        player.value = 0
        dealer.value = 0
        player.cards = []
        dealer.cards = []


        # Стартовая рука дилера
        dealer.add_card()
        dealer.print_value('дилера')
        temp_card = dealer.__str__()
        print(dealer.__str__())
        print(f'_______\n|xxxxx|\n|xxxxx|\n|xxxxx|\n|_____| \n')
        dealer.add_card()

        # Стартовая рука игрока
        player.add_card()
        temp_pcard = player.__str__()
        player.add_card()
        player.print_value('игрока')
        print(player.__str__())
        print(temp_pcard)

        # Ход Игрока


        if player.value == 21:
            print('Вы выиграли! У вас 21')
            chip.win_bet()
            game_on = False
            break

        player_input = input('Хотите взять еще карту? Y or N').lower()

        while player_input == 'y':
            player.add_card()
            print(player.__str__())
            player.print_value('игрока')
            if player.value > 21:
                break
            player_input = input('Хотите взять еще карту? Y or N').lower()
        if player.value > 21:
            print('У Вас перебор! Вы проиграли!')
            chip.lose_bet()
            game_on = False
            break

        # Ход Диллера
        print(temp_card)
        print(dealer.__str__())

        if dealer.value == 21:
            print('У диллера 21! Вы проиграли!')
            chip.lose_bet()
            break

        while dealer.value <17:
            dealer.add_card()
            print(dealer.__str__())

        dealer.print_value('дилера')
        player.print_value('игрока')

        if dealer.value > 21:
            print('У диллера перебор! Вы выиграли')
            chip.win_bet()
            break

        elif player.value > dealer.value:
            print('Вы победили!')
            chip.win_bet()
            game_on = False
            break
        elif player.value < dealer.value:
            print('Вы проиграли!')
            chip.lose_bet()
            game_on = False
            break
        else:
            print('Ничья!')
            game_on = False
            break




