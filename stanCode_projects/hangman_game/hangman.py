"""
File: hangman.py
Name: Ada Wang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Pick a random word first, and the player have n turns to guess.
    """
    answer = random_word()
    ans = hang_man(answer)


def hang_man(answer):
    """
    :param answer: str
    :return deciphered_str: str
    """
    dashed = ''
    input_ch = ''  # input a str each time
    guess = N_TURNS   # N_TURNS chances to try
    for i in range(len(answer)):
        dashed += '-'
    while True:
        print('The word looks like:' + dashed)
        print('You have ' + str(guess) + ' guesses left')
        input_ch = input('Your guess: ').upper()
        if input_ch.isalpha() == False:
            print('illegal format')
        elif len(input_ch) > 1:
            print('illegal format')
        elif answer == dashed:
            print(answer)
            print(dashed)
            print('You are correct!')
            print('You win!!')
            print('The word was: ' + dashed)
        elif answer.find(input_ch.upper()) == -1:
            print('There is no ' + input_ch + '\'s in the word.')
            guess = guess - 1
            if guess == 0:
                print('You are completely hung :( :(')
                print('The word was: ' + answer)
                break
        else:
            new_dashed = ''
            for i in range(len(answer)):
                if answer[i] == input_ch:
                    # when the user input is correct
                    new_dashed += input_ch
                elif dashed[i].isalpha() == True:
                    # keep the correct alpha
                    new_dashed += dashed[i]
                else:
                    new_dashed += '-'
            dashed = new_dashed
            if dashed == answer:
                print('You are correct!!')
                print('You win!!')
                print('The word was: ' + dashed)
                break
            else:
                print('You are correct!')

def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
