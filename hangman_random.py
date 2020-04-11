import re
import random


# Lists the index of a duplicate in a string
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


# The game itself
def game():
    lineNum = 1 # Starting line number
    f = open("words.txt", "r") # Opens words.txt.
    randomWord = random.randint(1,370103) # Chooses a random line number
    # Selects the answer randomly
    for x in f:
        if lineNum == randomWord:
            answer = x[:-1] #[:-1] removes the blankspace at the end of the word
        lineNum += 1
    # If the input is not an int, restarts loop
    while True:
        try:
            maxStrikes = int(input('Please input the maximum amount of strikes (0 for none): ')) 
            break
        except:
            print("Invalid value.")
    # If maxStrikes is chosen to be 0, it "removes" the limit by making the value really big.
    # 200IQ programming right there, folks.
    if maxStrikes == 0:
        maxStrikes = 999999
    underscoreAmount = 0 # Amount of underscores/symbols to hide the word with in-game
    letterArray = [] # Contains each letter of the word in an array, in the correct order
    for i in answer:
        letterArray.append(i)
        underscoreAmount += 1
    gameword = "-" * underscoreAmount # The hidden word, to be revealed
    strikes = 0 # Strikes
    guesses = [] # Correct letters
    misses = [] # Incorrect letters
    while answer != gameword:
        # Loads the game stats
        print(gameword)
        print()
        print("Strikes: " + str(strikes))
        print("Correct Letters: " + str(guesses).strip('[]'))
        print("Wrong Letters: " + str(misses).strip('[]'))
        print()
        letter = input("Input a letter: ").lower()
        # Checks for valid input (1 character, a-z)
        if not re.match("^[a-z]*$", letter):
            print("Invalid character.")
            continue
        elif len(letter) > 1:
            print("Too many characters.")
            continue
        # Checks if letter is already guessed
        if letter in guesses:
            print("Already guessed!")
            continue
        elif letter in misses:
            print("Already guessed!")
            continue
        # Checks if the letter is in the answer
        if letter in letterArray:
            print("Correct!\n")
            guesses.append(letter)
            tempList = list(gameword)
            letterPos = list_duplicates_of(answer,letter)
            for i in letterPos:
                tempList[i] = letter
            gameword = "".join(tempList)
        elif letter not in letterArray:
            print("Wrong!\n")
            misses.append(letter)
            strikes += 1
        # Checks result, determines if it's a W or an L based on strikes
        if strikes >= maxStrikes:
            print("You lose!")
            print("The word was: " + answer)
            break
    if strikes < maxStrikes:
        print()
        print("You Win!")
        print("The word was: " + answer)
        print("You finished with " + str(strikes) + " strikes!")
        print()


game() # Starts the game
while True:
    playAgain = input("Play again? (y/n) ")
    if playAgain.upper() == 'Y':
        game()
    elif playAgain.upper() == 'N':
        break
    else:
        print("Invalid response.")

# Made by FlamingLeo, April 2020
