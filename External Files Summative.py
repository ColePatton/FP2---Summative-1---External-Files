#------------------------------------------
# External Files Summative
# Cole Patton
#------------------------------------------

# Gets a highscore by rolling a random number and appends it to the file
# Can load this data for the user when they wish
# -----------------------------------------

#Imported random so that it can roll a random number used for the high scores
import random

# Imported time so that viewing things is easier and nice and slow for the user to comprehend.
import time

#--------------Functions Defined Here-----------------------

# Function for adding the number that the user rolled to the text file.
def append_score(name, number):
    print(f"You got the highscore of {number}, nice!")
    adding = open('highest number.txt', 'a')
    adding.write(f"\n{name}'s Highscore of: {number}")

# Function for the actual rolling of the number. Getting the random number.
def rolling_number():
    random_number = int(random.randint(0, 1000000))
    print("You rolled the number", random_number)
    return random_number

# Function for viewing all of the highscores the user has
def view_scores():
    print("Okay, checking scores!:")
    time.sleep(1)
    file = open('highest number.txt', 'r')
    scores = file.read()
    print(scores)
    time.sleep(5)

# Function for rolling a random number, that gets from the text file
def roll_number():
    random_number = rolling_number()
    time.sleep(2)
    append_score(user_name, random_number)
    time.sleep(2)
    
# Function for resetting the scores in the txt file
def reset_scores():
    resetting = open('highest number.txt', 'w')
    resetting.write("HIGH SCORES BELOW \n")
    

#-------------Main Code----------------
    
# My main code that asks each question for what the user would like to do
# The user can roll a number to be added to the scores,
# Quit out of the program
# View the scores
# Or lastly, the user can even reset the scores so that the txt file is back to 0
user_name = input("What is your name?")
go = True
while go == True:
    repeat = input("""What do you want to do?
    1 - Roll a Number! (Play the game)
    2 - Quit
    3 - View High Scores
    4 - Reset List of High Scores
    """)
    # This rolls the number for the score
    if repeat == '1':
        roll_number()
        go = True
    
    # This quits out of the program
    elif repeat == '2':
        go = False
        print("Bye!")
    
    # This views the scores of the txt file
    elif repeat == '3':
        view_scores()
        go = True
    
    # This resets the scores of the txt file
    elif repeat == '4':
        reset_scores()
        go = True
    
    
        

