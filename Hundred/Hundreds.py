
#Name: Pravin Jeyaraj
#A game called "Hundreds", where a player wins by being the first to reach 100 by rolling a dice.

import random

def instructions ():
    # This function displays the rules of the game on the screen.
    print('\"Hundreds\" is a two player game, where the goal is to be first one to reach a score of 100. Each player throws a die any number of times and,')
    print('a player\'s score for their turn is calculated by adding together the value of the die on each roll. However, if a player throws a is \'1\', their')
    print('turn comes to an end and their score for that turn is zero. A player\'s score for a turn, whether 0 or the sum of die rolls, is added to their total')
    print('score. This continues until one player scores at least 100.')
    print('\n')
    print('In this version of the game, you play against the computer and the computer goes first. So if the computer reaches 100 first, you get an extra')
    print('turn, so that you both have an equal number of turns. The value on the die is generated randomly.')

def roll():
    # This function generates a random integer value between 1 and 6 and returns it to simulate die roll.
    die_value = random.randint(1,6)
    return die_value

def computer_move (computer_score,human_score):
    # This function deals with one move by the computer. At tbe beginning, it sets the score for that turn to 0. It simulates the roll of the die and stores in
    # die_value by calling the roll () function. If the die value is 1, turn_score is set to 0 and Finished is set to True. Otherwise, the die value keeps being
    # added to turn_score. As long as the die_value thrown is not 1, the function checks to see if the computer is beating the human. But the computer does not
    # stop as soon as its score for that turn puts it ahead. Instead, the function generates a random numbet between 0 and 100 and the computer only stops if that
    # number is even. The aim of using the random number generator here is to make the computer appear more human by appearing to be take more risks - there is a 50%
    # chance that the computer keeps rolling even if it has scored enough on that round to be ahead of the human.
    turn_score = 0
    Finished = False
    while not Finished:
        die_value = roll() 
        print('The computer has rolled', die_value)
        if die_value == 1:
            turn_score = 0
            Finished = True
        else:
            turn_score = turn_score + die_value
            if computer_score + turn_score > human_score:
                stop = random.randint(0,100)
                if stop % 2 == 0:
                    Finished = True
        print('The computer\'s score for this turn so far is', turn_score)
        print('The computer\'s total score is', turn_score + computer_score)
    return turn_score

def human_move (computer_score,human_score):
    # This function deals with one move by the human player. At tbe beginning, it sets the score for that turn to 0. The human is asked whether they want to roll, 
    # by calling ask_yes_or_no (). If roll_again is True, the function simulates the roll of the die and stores it in die_value by calling the roll() function.
    # If the die value is 1, turn_score is set to 0 and Finished is set to True. Otherwise, the die value is added to turn_score and the human is given the option to
    # roll again. If the human does not want to roll again (set to False), then Finished is set to True.
    turn_score = 0
    print('Your score is:', human_score)
    print('The computer\'s score is:', computer_score)
    score_difference = computer_score - human_score
    if score_difference > 0:
        print('The computer is ahead by:', score_difference)
    elif score_difference < 0:
        print('You are ahead by:', abs(score_difference))
    else:
        print('You and the computer are currently tied')
    Finished = False
    while not Finished:
        roll_again = ask_yes_or_no('Do you want to roll again?')
        if roll_again == True:
            die_value = roll()
            print('You have rolled', die_value)
            if die_value == 1:
                turn_score = 0
                Finished = True
            else:
                turn_score = turn_score + die_value
        else:
             Finished = True
        print('You score for this turn so far is', turn_score)
        print('Your total score is', turn_score + human_score)
    return turn_score

def ask_yes_or_no (prompt):
    # This function is called from human_move (). It has to check the value input by the user. It makes an initial assumption that the user input will have an error,
    # and sets error to True. It asks the user for input and then converts to a string - this makes sure that pressing return without inputting anything does not
    # produce an error. Instead, the lack of input is converted into an empty string. The function can then check the first character of the string. If the first
    # character is a lower or upper case 'y' or 'n', the roll_again is set to True or False respectively and error is set to False. Otherwise, including if it is an
    # empty string, the user is asked again for input. The function returns roll_again.
    error = True
    while error == True:
        yes_or_no = str(input(prompt))
        if yes_or_no == (''):            print('Sorry, I don\'t understand')
        elif yes_or_no[0] == ('y') or yes_or_no[0] == ('Y'):
            roll_again = True
            error = False
        elif yes_or_no[0] == ('n') or yes_or_no[0] == ('N'):
            roll_again = False
            error = False
        else:
            print('Sorry, I don\'t understand')
    return roll_again

def is_game_over (computer_score,human_score):
    # The function is called from the main function. It checks to see whether either the computer or the human player has scored 100 or more and sets Finished to
    # True or False, indicating whether the game is over or whether anyone can roll again.
    if computer_score > 100 or human_score > 100: # one or both has scored more than 100. 
        Finished = True
    elif computer_score >= 100 and human_score < 100: # the computer had scored at least 100, the human has not.
        Finished = True
    elif computer_score < 100 and human_score >= 100: # the human has scored at least 100, the computer has not.
        Finished = True
    elif computer_score == human_score == 100: # both the computer and the human player are tied on 100 (tie needs to be broken).
        Finished = False
    else:   # neither the computer nor the human player has reached 100 and so can continue playing. 
        Finished = False
    return Finished

def show_results(computer_score,human_score):
    # This function is called from main(), once is_game_over() returns Finished = True. It calculates the difference between the computer and the human's score.
    # Depending on whether the computer has scored more or less than 100 and whether the human has scored more or less than 100, the function returns an appropriate
    # message.
    score_difference = computer_score - human_score
    if computer_score >= 100:
        if human_score < 100:
            print('Sorry, you lost to the computer by', abs(score_difference))
        else:
            print('Sorry, you score 100 or more but lost to the computer by', abs(score_difference))
    elif human_score >= 100:
        print('Congratulations, you beat the computer by', abs(score_difference))

def main():
    # This is the main function, representing the game. First the computer and human's scores are set to 0 and the instructions for the game are displayed.
    # Then the computer has a turn, followed by the human and the functions checks to see whether the game is over (Finished = True). The process is repeated as
    # long as Finished is False. When the game is finished, the results are displayed. 
    computer_score = 0
    human_score = 0
    instructions()
    Finished = False
    while not Finished:
        print('\n')
        print('It is the computer\'s turn')
        computer_score = computer_score + computer_move(computer_score,human_score)
        print('\n')
        print('It is your turn')
        human_score = human_score + human_move(computer_score,human_score)
        Finished = is_game_over(computer_score,human_score)
    print('\n')
    show_results(computer_score, human_score)

main()

