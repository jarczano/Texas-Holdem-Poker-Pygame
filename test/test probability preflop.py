import random
import time

from app.player_class import Player
from app.poker_score import players_score

# Test, how many rounds should be played to see which probability given hand is to win pre-flop
deck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC', '2S', '3S', '4S',
        '5S',
        '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', '2H', '3H', '4H', '5H', '6H', '7H', '8H',
        '9H',
        'TH', 'JH', 'QH', 'KH', 'AH', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD',
        'KD', 'AD']


start = time.time()
start_stack = 100
alice = Player('Alice', start_stack)
bob = Player('Bob', start_stack)
players_list = [alice, bob]

alice.cards = ['AC', 'AD']

number_round = 5000
n_win = 0
n_tie = 0

for i in range(number_round):
    deck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', '2S', '3S', '4S', '5S', '6S',
            '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH',
            'QH', 'KH', 'AH', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']

    bob.cards = random.sample(deck, 2)
    [deck.remove(bob.cards[i]) for i in range(2)]
    table = random.sample(deck, 5)
    [deck.remove(table[i]) for i in range(5)]
    players_score(players_list, table)
    if alice.score > bob.score:
        n_win += 1
    elif alice.score == bob.score:
        n_tie += 1
stop = time.time()

print(n_win / number_round)

print('Time: ', stop - start)

