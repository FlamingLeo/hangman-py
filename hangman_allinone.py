import re
import getpass
import random


# Lists the index of a duplicate in a string
def list_duplicates_of(seq, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at + 1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


# Gamemodes: Multiplayer, Singleplayer, Singleplayer Simplified
def gamemode():
    print("Choose a gamemode.")
    print("A: Local Multiplayer")
    print("B: Singleplayer")
    print("C: Singelplayer (easy)")
    print()
    # Prompt user to choose a valid option
    while True:
        option = input("Choose an option: ")
        if option.upper() == 'A':
            break
        elif option.upper() == 'B':
            break
        elif option.upper() == 'C':
            break
        else:
            print("Invalid option.")
    # Different functionalities based on choice
    lineNum = 1  # Global starting line number
    if option.upper() == 'A':
        answer = getpass.getpass("Please input a word (lowercase a-z): ")  # The chosen word
        # If the answer is not valid, repeat the input until it's valid
        while re.match("^[a-z]*$", answer) is None:
            answer = getpass.getpass("Invalid word. Try again: ")
        return answer
    if option.upper() == 'B':
        f = open("words.txt", "r")  # Opens words.txt.
        randomWord = random.randint(1, 370103)  # Chooses a random line number
        # Selects the answer randomly
        for x in f:
            if lineNum == randomWord:
                answer = x[:-1]  # [:-1] removes the blankspace at the end of the word
            lineNum += 1
        return answer
    if option.upper() == 'C':
        f = open("words_simplified.txt", "r")  # Opens words.txt.
        randomWord = random.randint(1, 61336)  # Chooses a random line number
        # Selects the answer randomly
        for x in f:
            if lineNum == randomWord:
                answer = x[:-1]  # [:-1] removes the blankspace at the end of the word
            lineNum += 1
        return answer
            

# The game itself
def game():
    answer = gamemode()
    # If the input is not an int, restarts loop
    while True:
        try:
            maxStrikes = int(input('Please input the maximum amount of strikes (0 for none): '))
            break
        except:
            print("Invalid value.")
    # If maxStrikes is chosen to be 0, it "removes" the limit by making the value really big.
    # There's definitely a better way to do this, but I CBA.
    if maxStrikes == 0:
        maxStrikes = 999999
    underscoreAmount = 0  # Amount of underscores/symbols to hide the word with in-game
    letterArray = []  # Contains each letter of the word in an array, in the correct order
    for i in answer:
        letterArray.append(i)
        underscoreAmount += 1
    gameword = "-" * underscoreAmount  # The hidden word, to be revealed
    strikes = 0  # Strikes
    guesses = []  # Correct letters
    misses = []  # Incorrect letters
    while answer != gameword:
        # Loads the game stats
        print()
        print(gameword)
        print()
        print("Strikes: " + str(strikes))
        print("Correct Letters: " + str(guesses).strip('[]'))
        print("Wrong Letters: " + str(misses).strip('[]'))
        print()
        letter = input("Input a letter: ").lower()
        # Give up
        if letter == "stop":
            print()
            print("You lose!")
            print("The word was: " + answer)
            break
        # Checks for valid input (1 character, a-z)
        if not re.match("^[a-z]*$", letter):
            print("Invalid character.")
            continue
        elif len(letter) > 1:
            print("Too many characters.")
            continue
        elif len(letter) == 0:
            print("Please input a character.")
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
            letterPos = list_duplicates_of(answer, letter)
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
    if strikes < maxStrikes and letter != "stop":
        print()
        print("You Win!")
        print("The word was: " + answer)
        print("You finished with " + str(strikes) + " strikes!")
        print()


game()  # Starts the game
while True:
    playAgain = input("Play again? (y/n) ")
    if playAgain.upper() == 'Y':
        print()
        game()
    elif playAgain.upper() == 'N':
        break
    else:
        print("Invalid response.")

# Made by FlamingLeo, April 2020
