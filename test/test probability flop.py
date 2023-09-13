import random

# Test, how many rounds should be played to see which probability given hand is to win flop
deck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC', '2S', '3S', '4S', '5S', '6S',
        '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH',
        'QH', 'KH', 'AH', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD']


start_stack = 100
alice = PlayerClass.Player('Alice', start_stack, 0)
bob = PlayerClass.Player('Bob', start_stack, 1)
players_list = [alice, bob]

alice.cards = ['JC', '5C']

number_round = 5000
n_win = 0
n_tie = 0
history = [i for i in range(number_round)]
history_win = [0 for i in range(number_round)]

flop = ['2D', '9D', 'AD']
for i in range(number_round):
    deck = ['2C', '3C', '4C', '6C', '7C', '8C', '9C', 'TC', 'QC', 'KC', 'AC', '2S', '3S', '4S', '5S', '6S',
            '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH',
            'QH', 'KH', 'AH', '3D', '4D', '5D', '6D', '7D', '8D', 'TD', 'JD', 'QD', 'KD']

    bob.cards = random.sample(deck, 2)
    [deck.remove(bob.cards[i]) for i in range(2)]

    table = random.sample(deck, 2)
    [deck.remove(table[i]) for i in range(2)]
    table += flop

    Poker_score.players_score(players_list, table)
    if alice.score > bob.score:
        n_win += 1
    elif alice.score == bob.score:
        n_tie += 1

    history_win[i] = n_win / (i + 1)
print(history_win[number_round-1])


'''
import matplotlib.pyplot as plt
import numpy as np

#mean = np.mean(history_win[5000:])
#median = np.median(history_win[5000:])
mean = np.mean(history_win[1000:])
median = np.median(history_win[1000:])
print('mean: ', mean * 100)
print('median: ', median * 100)

#plt.plot(history[5000:], history_win[5000:])
plt.axhline(y=mean, color='blue', linestyle='--')
plt.axhline(y=median, color='black', linestyle=':')
plt.plot(history, history_win)
plt.xlabel('number of rounds')
plt.ylabel('percent of wins')
plt.show()

'''
