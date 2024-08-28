import random
def rps():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]
    game_images = [paper, rock, scissors]

    user_input = input('Paper, rock, or scissors?').lower()
    options = ['paper','rock','scissors']
    my_guess = random.choice(options)

    print(game_images[my_guess])

    return

    if my_guess == 'scissors':
        ascii_art = scissors
    elif    my_guess == 'rock':
        ascii_art = rock
    else:
        ascii_art = paper


    if user_input == my_guess:
        print("draw, try again!")
    elif user_input == 'scissors' and my_guess == 'paper':
        print(f'you win! I guessed: \n{ascii_art}')
    elif user_input == 'paper' and my_guess == 'rock':
        print(f'you win! I guessed: \n{ascii_art}')
    elif user_input == 'rock' and my_guess == 'scissors':
        print(f'you win! I guessed: \n{ascii_art}')
    else:
        print(f'I win! I guessed {my_guess} but you guessed {user_input}')
        print(ascii_art)
    rps()

rps()