import random
from dis import code_info


def coin_toss():
    random_value = random.randint(1, 100)
    your_guess = input('Heads or tails?').lower()

    print(random_value)

    if random_value % 2 == 0:
        coin_flip = 'heads'
    else:
        coin_flip = 'tails'

    if your_guess == coin_flip:
        print(f'{coin_flip} - you win!')
        coin_toss()
    else:
        print(f'{coin_flip} - you lose :(')
        coin_toss()

coin_toss()