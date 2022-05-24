#
# Python:       3.10.4
#
# Author:       Hunter L. Grayson
#
# Purpose:      The Tech Academy - Python Course, creating our first program together.
#               Demonstrating how to pass variables from function to function
#               while producing a functional game
#               
#               Remember, function_name(variable) _means that we pass in the variable.
#               return variable _means that we are returning the variable to
#               back to the calling function.



def start (fight=0,run=0,name="") :
    # get user's name
    name = describe_game(name)
    fight,run,name = fight_run(fight,run,name)

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will ambushed \nby several different people. \nYou can choose to be fight or run")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
            
    return name



def fight_run(fight,run,name):
    stop = True
    while stop:
        show_score(fight,run,name)
        pick = input("\nA vigilante approaches \nconversation. Will you fight or \nor run? (F/R) \n>>>: ").lower()
        if pick == "f":
            print("\nThe vigilante walks away smiling...")
            fight = (fight + 1)
            stop = False
        if pick == "r":
            print ("\nThe vigilante stares at you \nas you escape...")
            run = (run + 1)
            stop = False
        score(fight,run,name) #pass the 3 variables to the score()

def show_score(fight,run,name):
    print ("\n{}, your current total: \n({}, fight) and ({}, run)".format(name,fight,run))


def score(fight,run,name):
    # score function is being passed the values stored within the 3 variables
    if fight > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(fight,run,name)
    if run > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(fight,run,name)
    else:       #else, call fight_run function passing in the variables so it can use them
        fight_run(fight,run,name)


def win(fight,run,name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nLike the smart person you are\nyou've escaped from any danger!".format(name))
    # call again function and pass in our variables
    again(fight,run,name)


def lose(fight,run,name):
    # Substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game over! \n{}, you hung around and fought a vigilante too though, Unlucky!".format(name))
    # Substitute the {} wildcards with our variable values
    again(fight,run,name)

    
def again(fight,run,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(fight,run,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")


def reset(fight,run,name):
    fight = 0
    run = 0
    #Notice, I do not reset the name variable as that same user has elected to play again.
    start(fight,run,name)


if __name__ == "__main__":
    start()
