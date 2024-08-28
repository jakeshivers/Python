
def script():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("you can ride this ride" )
    else:
        print("You cannot ride this ride")

    restart = input('Would you like to restart?')
    if restart == 'y':
        print("restarting")
        script()
    else:
        print('Boodbye')

script()