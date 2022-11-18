
import random

import colorama
from colorama import Fore, Back, Style # |> importing colorama for styling output

colorama.init(autoreset=True)

"""
Fore : RED, BLACK, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back : RED, BLACK, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style : DIM, NORMAL, BRIGHT, RESET_ALL.
"""


exit = False
user_point = 0
computer_point = 0


while exit == False:
    options = ["rock", "paper", "scissor"]
    user_input = input(Fore.CYAN + Style.BRIGHT + 'Choose rock, paper, scissor or exit :  \n')
    computer_input = random.choice(options)

    if user_input == 'exit':
        print('Game Ended \n')
        print(f"User Score : {user_point}, Computer Score : {computer_point}")
        exit = True

    elif user_input == 'rock':
        if computer_input == 'rock':
            print('your input is Rock')
            print('Computer input is Rock')
            print(Fore.YELLOW + Style.BRIGHT + 'It is a tie \n')

        elif computer_input == 'paper':
            print('your input is Rock')
            print('Computer input is Paper')
            print(Fore.RED + Style.BRIGHT + 'Computer wins \n')
            computer_point +=1

        elif computer_input == 'scissor':
            print('your input is Rock')
            print('Computer input is Scissor')
            print(Fore.GREEN + Style.BRIGHT + 'You win \n')
            user_point +=1

    elif user_input == 'paper':
        if computer_input == 'rock':
            print('your input is Paper')
            print('Computer input is Rock')
            print(Fore.GREEN + Style.BRIGHT + 'You win \n')
            user_point +=1

        elif computer_input == 'paper':
            print('your input is Paper')
            print('Computer input is Paper')
            print(Fore.YELLOW + Style.BRIGHT + 'Its a tie')

        elif computer_input == 'scissor':
            print('your input is Paper')
            print('Computer input is Scissor')
            print(Fore.RED + Style.BRIGHT + 'Computer wins \n')
            computer_point +=1
    elif user_input == 'scissor':
        if computer_input == 'rock':
            print('your input is scissor')
            print('Computer input is Rock')
            print(Fore.RED + Style.BRIGHT + 'Computer wins \n')
            computer_point +=1

        elif computer_input == 'paper':
            print('your input is scissor')
            print('Computer input is Paper')
            print(Fore.GREEN + Style.BRIGHT + 'You win \n')
            user_point +=1

        elif computer_input == 'scissor':
            print('your input is scissor')
            print('Computer input is Scissor')
            print(Fore.YELLOW + Style.BRIGHT + 'Its a tie \n')

    elif user_input != 'rock' or user_input != 'paper' or user_input !=  'scissor':
        print(Back.RED + 'Invalid input \n')