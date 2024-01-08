import random  # importing the randmom libaray to use the 'randmon.choice' function

def get_choices():  # defining get_choices function
    player_choice = input("Enter a choice (rock, paper, scissors) ")  # getting input for the user 
    options = ["rock", "paper", "scissors"]  # setting the options 

    computer_choice = random.choice(options)  # making the computer choose use the random libaray
    choices = {"player" : player_choice, "computer": computer_choice}  # setting the dictionary with our key valuses

    return choices  # returning the dictionary

def check_win(player, computer):
    # print(f"You chose {player} and Computer chose {computer}")  # both prints work the same but i chose the old way to continues\
    print("You chose {} and Computer chose {}".format(player, computer)) 

    '''
    Now we will do some checks to see who will win
    if player choice equals to computer choice it will be a tie
    else check all the result using nested if to see who will win

    '''
    if player == computer:
        print("It's a Tie")  # i think i should have used return instead of print.. i don't know know :(
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes Scissors, You Win!")
        else:
            print("Paper covers Rock, You Lose.")
    elif player == "paper":
        if computer == "rock":
            print("Paper covers Rock, You Win!")
        else:
            print("Scissors cuts Paper, You Lose.")
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts Paper, You Win!")
        else:
            print("Rock smashes Scissors, You Lose")

choices_dictionary = get_choices()  #
# assigning a variable to check_win function and displaying the result /
result = check_win(choices_dictionary["player"], choices_dictionary["computer"])  

