import random
import my_module
my_number =random.randint(1, 100)
guesses_remaining = 3
low_guesses = [0]
high_guesses = [100]

print(my_module.my_favorite_number)

while guesses_remaining !=0:
    your_guess = int(input('Guess my number. It is between 1 and 100\n'))
    if your_guess > my_number:
        print('Lower')
        high_guesses.append(your_guess)
    elif your_guess < my_number:
        print('higher')
        low_guesses.append(your_guess)
    else:
        print('You win!')
        break

    guesses_remaining = guesses_remaining -1
    if guesses_remaining == 0:
        print(f'Sorry, you ran out of guesses.'
              f'The answer is {my_number}')
        break
    print(f'You have {guesses_remaining} left.'
          f'\nHere are the guesses you'f've made so far: {low_guesses + high_guesses}'
          f'\nYour guess must be between: {max(low_guesses)} '
          f'and {min(high_guesses)}')

random.uniform()