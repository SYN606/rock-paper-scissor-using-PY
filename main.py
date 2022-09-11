
import random

exit = False
user_point = 0
computer_point = 0


while exit == False:
    options = ["rock", "paper", "scissor"]
    user_input = input('Choose rock, paper, scissor or exit :  \n')
    computer_input = random.choice(options)

    if user_input == 'exit':
        print('Game Ended \n')
        print(f"User Score : {user_point}, Computer Score : {computer_point}")
        exit = True

    elif user_input == 'rock':
        if computer_input == 'rock':
            print('your input is Rock')
            print('Computer input is Rock')
            print('It is a tie \n')

        elif computer_input == 'paper':
            print('your input is Rock')
            print('Computer input is Paper')
            print('Computer wins \n')
            computer_point +=1

        elif computer_input == 'scissor':
            print('your input is Rock')
            print('Computer input is Scissor')
            print('You win \n')
            user_point +=1

    elif user_input == 'paper':
        if computer_input == 'rock':
            print('your input is Paper')
            print('Computer input is Rock')
            print('You win \n')
            user_point +=1

        elif computer_input == 'paper':
            print('your input is Paper')
            print('Computer input is Paper')
            print('Its a tie')

        elif computer_input == 'scissor':
            print('your input is Paper')
            print('Computer input is Scissor')
            print('Computer wins \n')
            computer_point +=1
    elif user_input == 'scissor':
        if computer_input == 'rock':
            print('your input is scissor')
            print('Computer input is Rock')
            print('Computer wins \n')
            computer_point +=1

        elif computer_input == 'paper':
            print('your input is scissor')
            print('Computer input is Paper')
            print('You win \n')
            user_point +=1

        elif computer_input == 'scissor':
            print('your input is scissor')
            print('Computer input is Scissor')
            print('Its a tie \n')

    elif user_input != 'rock' or user_input != 'paper' or user_input !=  'scissor':
        print('Invalid input \n')