# https://github.com/4ttth
# Support this project by giving me a coffee
#
# Made with 💗 by 4ttth
import json
import random

docstring = '''
HAUngman is a basic python game script that is based off the traditional game 'Hangman'.
HAUngman is specifically inclined for Holy Angel University's dictionary
HAUngman also offers a text-based multiplayer command-line that can range from many players!
HAUngman offers 3 different singleplayer modes:
1) HAU without hint
2) HAU with hint
3) Regular dictionary (500 words)

This code is open-source, feel free to edit, fork, or repo.
'''


def clear():
    for i in range(1, 200):
        i = ""
        print(i)


def wrongman(number):
    if number == 1:
        hangman1()
    elif number == 2:
        hangman2()
    elif number == 3:
        hangman3()
    elif number == 4:
        hangman4()
    elif number == 5:
        hangman5()
    elif number == 6:
        hangman6()


def hangman0():  # base
    print("*------*  ")
    print("|      !  ")
    print("|         ")
    print("|         ")
    print("|         ")
    print("|         ")
    print("*========|")


def hangman1():  # wanswer1
    print("*------*  ")
    print("|      !  ")
    print("|      O  ")
    print("|         ")
    print("|         ")
    print("|         ")
    print("*========|")


def hangman2():  # wanswer2
    print("*------*  ")
    print("|      !  ")
    print("|      O  ")
    print("|      |  ")
    print("|         ")
    print("|         ")
    print("*========|")


def hangman3():  # wanswer3
    print("*------*  ")
    print("|      !  ")
    print("|      O  ")
    print("|     /|  ")
    print("|         ")
    print("|         ")
    print("*========|")


def hangman4():  # wanswer4
    print("*------*  ")
    print("|      !  ")
    print("|      O  ")
    print("|     /|\ ")
    print("|         ")
    print("|         ")
    print("*========|")


def hangman5():  # wanswer5
    print("*------*  ")
    print("|      !  ")
    print("|      O  ")
    print("|     /|\ ")
    print("|      |  ")
    print("|         ")
    print("*========|")


def hangman6():  # wanswer6
    print("*------*  ")
    print("|      !  ")
    print("|      O  ")
    print("|     /|\ ")
    print("|      |  ")
    print("|      ^  ")
    print("*========|")
    print("Mr. HAUngman died, player 1 wins!")
    a = str(input("Would you like to try again? "))
    if 'y' or 'Y' in a:
        clear()
        intro()
    elif 'n' or 'N' in a:
        clear()
        print("*" * 26)
        a2 = "  _  _   _   _   _   _     "
        print(a2)
        a3 = " | || | | |_| |_| |_| |__  "
        print(a3)
        a4 = " | || |_| __| __| __| '_ \ "
        print(a4)
        a5 = " |__   _| |_| |_| |_| | | | "
        print(a5)
        a6 = "    |_|  \__|\__|\__|_| |_|"
        print(a6)
        print("*" * 26)
        print("")
        print("Thank you for playing HAUngman!")
        print("Made with 💗 by https://github.com/4ttth")


def outro():
    print("*" * 26)
    a2 = "  _  _   _   _   _   _     "
    print(a2)
    a3 = " | || | | |_| |_| |_| |__  "
    print(a3)
    a4 = " | || |_| __| __| __| '_ \ "
    print(a4)
    a5 = " |__   _| |_| |_| |_| | | | "
    print(a5)
    a6 = "    |_|  \__|\__|\__|_| |_|"
    print(a6)
    print("*" * 26)
    print("")
    print("Thank you for playing HAUngman!")
    print("Made with 💗 by https://github.com/4ttth")
    a = input("Would you like to try again?").upper()
    if 'Y' in a:
        intro()
        gamesel()
    else:
        print("Thank you for playing HAUngman!")
        print("Made with 💗 by https://github.com/4ttth")
        print("Exitting program now...")
        exit()


def intro():    # code by: 4ttth :)
    print("*" * 26)
    a2 = "  _  _   _   _   _   _     "
    print(a2)
    a3 = " | || | | |_| |_| |_| |__  "
    print(a3)
    a4 = " | || |_| __| __| __| '_ \ "
    print(a4)
    a5 = " |__   _| |_| |_| |_| | | | "
    print(a5)
    a6 = "    |_|  \__|\__|\__|_| |_|"
    print(a6)
    print("*" * 26)
    print("")
    print("Welcome to HAUngman! A basic python script game made by 4ttth.")
    print("Accessible through: https://github.com/4ttth")
    print("")


def gamesel():
    print("-" * 26)
    print("Please select a game mode: ")
    print("     [1] Singleplayer")
    print("     [2] Multiplayer")
    print("-" * 26)
    global gameselInput
    try:
        gameselInput = int(input("Game mode: "))
        if gameselInput == 1:
            clear()
            dictsel()
        elif gameselInput == 2:
            clear()
            multiplayer()
        else:
            clear()
            print("-" * 26)
            print(f"Invalid game mode: {gameselInput}, kindly select either '1' or '2'. ")
            gamesel()
    except NameError:
        clear()
        print("-" * 26)
        print(f"Invalid game mode, kindly select either '1' or '2'. ")
        gamesel()
    except ValueError:
        clear()
        print("-" * 26)
        print(f"Invalid game mode, kindly select either '1' or '2'. ")
        gamesel()

def dictsel():
    print("-" * 26)
    print("Please select dictionary type: ")
    print("     [1] HAU")
    print("     [2] HAU with hints")
    print("     [3] Regular")
    print("-" * 26)
    global dictselInput
    try:
        dictselInput = int(input("Dictionary type: "))
        if dictselInput == 1 or dictselInput == 2 or dictselInput == 3:
            singleplayer()
        else:
            print(f"Invalid dictionary type: {dictselInput}, kindly select either '1', '2', or '3'.")
            dictsel()
    except NameError:
        print(f"Invalid dictionary type, kindly select either '1', '2', or '3'.")
        dictsel()
    except ValueError:
        print(f"Invalid dictionary type, kindly select either '1', '2', or '3'.")
        dictsel()

def singleplayer():
    with open('dictionary.txt') as f:
        data = f.read()
    with open('regdict.txt') as g:
        data2 = g.read()

    js = json.loads(data)
    js2 = json.loads(data2)
    global cAnswer
    global cDesc
    global cLength

    if dictselInput == 1:
        randomizer = str(random.randint(1, 9))
        cAnswer = str(js.get(randomizer))
        cLength = len(cAnswer)
        startsingle()
    if dictselInput == 2:
        randomizer = str(random.randint(1, 9))
        randomizerDesc = (randomizer + "desc")
        cAnswer = str(js.get(randomizer))
        cDesc = str(js.get(randomizerDesc))
        cLength = len(cAnswer)
        startsingle()
    elif dictselInput == 3:
        randomizer = str(random.randint(0, 500))
        cAnswer = str(js2.get(randomizer))
        cLength = len(cAnswer)
        startsingle()


def singleGuessWord1(sLetters):
    counter = 0
    cLetters1 = 0
    for char in cAnswer:
        if char in sLetters:
            print(cAnswer[counter], end=" ")
            cLetters1 += 1
        else:
            print(" ", end=" ")
        counter += 1
    return cLetters1


def singleGuessWord2():
    print("\r")
    for char in cAnswer:
        print("\u203E", end=" ")


def startsingle():
    clear()
    print("-" * 26)
    print(f"   You have selected SINGLEPLAYER! Goodluck!")
    print("    1) Your task is to guess the given word from the pool depending on your choice before.")
    print("    2) If you choose the option [2], you'll be given hints!")
    print("    3) You only have six tries before Mr. HAUngman dies.")
    print("    4) If you somehow guessed the word, you get a point and you win!")
    print("    5) Each time a guess is wrong, a body part of Mr. HAUngman will be shown.")
    print("    6) Mr. HAUngman will be declared dead once his leg is shown.")
    print("    7) If Mr. HAUngman dies, you lose!")
    print("-" * 26)
    y = input("Ready to begin? ")
    if 'y' in y or 'Y' in y:
        clear()
        print("-" * 26)
        startsing()
    elif 'n' in y or 'N' in y:
        clear()
        gamesel()
    else:
        clear()
        gamesel()


def startsing():
    print("-" * 26)
    hangman0()
    guessTurn1 = 0
    guessPool1 = []
    wrongCount1 = 0
    rightGuess1 = 0
    print("-" * 26)
    print("Your word is:")
    for x in cAnswer:
        print("_", end=" ")
    print("")
    if dictselInput == 2: print(f'\nHint: {cDesc}')
    print("-" * 26)
    while wrongCount1 != 6 and rightGuess1 != cLength:
        print("\nLetters used: ")
        for k in guessPool1:
            print(k, end=" ")
        print("")
        print("-" * 26)
        guess = str(input(f"Guess a letter or the word: "))
        guess = guess.upper()
        if len(guess) == cLength:
            if guess == cAnswer:
                clear()
                wrongman(wrongCount1)
                print("-" * 26)
                print(f"You have guessed the word!")
                outro()
            else:
                clear()
                print("-" * 26)
                print("Wrong guess!")
                print("-" * 26)
                wrongCount1 += 1
                wrongman(wrongCount1)
                rightGuess1 = singleGuessWord1(guessPool1)
                singleGuessWord2()
                if dictselInput == 2: print(f'\nHint: {cDesc}')
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessPool1:
                clear()
                print(f"You already guessed the letter: {guess}.")
                wrongman(wrongCount1)
                singleGuessWord2()
                if dictselInput == 2: print(f'\nHint: {cDesc}')

            elif guess not in cAnswer:
                clear()
                print("-" * 26)
                wrongCount1 += 1
                guessPool1.append(guess)
                wrongman(wrongCount1)
                rightGuess1 = singleGuessWord1(guessPool1)
                singleGuessWord2()
                if dictselInput == 2: print(f'\nHint: {cDesc}')

            else:
                clear()
                print("-" * 26)
                wrongman(wrongCount1)
                guessTurn1 += 1
                guessPool1.append(guess)
                rightGuess1 = singleGuessWord1(guessPool1)
                singleGuessWord2()
                if dictselInput == 2: print(f'\nHint: {cDesc}')

        elif len(guess) >= 2:
            clear()
            print("-" * 26)
            wrongCount1 += 1
            wrongman(wrongCount1)
            rightGuess1 = singleGuessWord1(guessPool1)
            singleGuessWord2()
            print("\nWrong guess!")
            if dictselInput == 2: print(f'\nHint: {cDesc}')

        elif len(guess) >= cLength:
            clear()
            print("-" * 2)
            wrongCount1 += 1
            wrongman(wrongCount1)
            rightGuess1 = singleGuessWord1(guessPool1)
            singleGuessWord2()
            print(f"Your guess has {len(guess)} letters, the correct answer only has {cLength} answers.")
            if dictselInput == 2: print(f'\nHint: {cDesc}')
    else:
        clear()
        print("-" * 26)
        wrongman(wrongCount1)
        print(f'You have guessed the last letter! The word is: {cAnswer}!')
        outro()


def multiplayer():
    print("-" * 26)
    global xplay
    try:
        xplay = int(input("You have selected: MULTIPLAYER, how many players will be playing today? "))
        print("-" * 26)
    except NameError:
        clear()
        print("-" * 26)
        print("Invalid input, must be an integer.")
        multiplayer()
    except ValueError:
        clear()
        print("-" * 26)
        print("Invalid input, must be an integer.")
        multiplayer()
    clear()
    print("-" * 26)
    print(f"   There are {xplay} players, with player 1 going first then player {xplay} going last.")
    print("    1) Player 1 will select a word, and will be guessed by everyone.")
    print("    2) The word given by Player 1 will be underscores, each letter to be guessed by the players.")
    print("    3) Each player will take turn in guessing either a letter or the word.")
    print("    4) Whichever guesses the word correctly, gets the point!")
    print("    5) Each time a guess is wrong, a body part of Mr. HAUngman will be shown.")
    print("    6) Mr. HAUngman will be declared dead once his leg is shown.")
    print("    7) If Mr. HAUngman dies, Player 1 wins!")
    print("-" * 26)
    y = input("Ready to begin? ")
    if 'y' in y or 'Y' in y:
        clear()
        print("-" * 26)
        startmulti()
    elif 'n' in y or 'N' in y:
        clear()
        gamesel()
    else:
        clear()
        gamesel()


def startmulti():
    global multiAnswer
    global malength
    global macensor
    multiAnswer = str(input("Player 1, pick any word: "))
    multiAnswer = multiAnswer.upper()
    malength = len(multiAnswer)
    print(f'Confirm that {multiAnswer} is your selected word?')
    y = input("")
    if 'y' in y or 'Y' in y:
        clear()
        print("-" * 26)
        startmultiguess()
    if 'n' in y or 'N' in y:
        clear()
        print("-" * 26)
        startmulti()
    else:
        startmulti()


def multiGuessWord1(gLetters):
    counter = 0
    cLetters = 0
    for char in multiAnswer:
        if char in gLetters:
            print(multiAnswer[counter], end=" ")
            cLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return cLetters


def multiGuessWord2():
    print("\r")
    for char in multiAnswer:
        print("\u203E", end=" ")


def startmultiguess():
    print("-" * 26)
    hangman0()
    guesser = 2
    guessTurn = 0
    guessPool = []
    wrongCount = 0
    rightGuess = 0
    print("-" * 26)
    print("Your word is:")
    for x in multiAnswer:
        print("_", end=" ")
    print("")
    print("-" * 26)
    # print(multiAnswer)
    # print(macensor)
    while wrongCount != 6 and rightGuess != malength:
        print("\nLetters used: ")
        for k in guessPool:
            print(k, end=" ")
        if guesser > xplay:
            guesser = 2
        print("")
        print("-" * 26)
        pguess = str(input(f"Player {guesser}, it is your turn to guess a letter or the word: "))
        pguess = pguess.upper()
        if len(pguess) == malength:
            if pguess == multiAnswer:
                clear()
                wrongman(wrongCount)
                print("-" * 26)
                print(f"Player {guesser} have guessed the word! The word is: {multiAnswer}!")
                outro()
            else:
                clear()
                print("-" * 26)
                print("Wrong guess!")
                print("-" * 26)
                guesser += 1
                wrongCount += 1
                wrongman(wrongCount)
                rightGuess = multiGuessWord1(guessPool)
                multiGuessWord2()
        elif len(pguess) == 1 and pguess.isalpha():
            if pguess in guessPool:
                clear()
                print(f"You already guessed the letter: {pguess}.")
                wrongman(wrongCount)
                rightGuess = multiGuessWord1(guessPool)
                multiGuessWord2()

            elif pguess not in multiAnswer:
                clear()
                print("-" * 26)
                wrongCount += 1
                guesser += 1
                guessPool.append(pguess)
                wrongman(wrongCount)
                rightGuess = multiGuessWord1(guessPool)
                multiGuessWord2()

            else:
                clear()
                print("-" * 26)
                wrongman(wrongCount)
                guesser += 1
                guessTurn += 1
                guessPool.append(pguess)
                rightGuess = multiGuessWord1(guessPool)
                multiGuessWord2()

        elif len(pguess) >= 2:
            clear()
            print("-" * 26)
            guesser += 1
            wrongCount += 1
            wrongman(wrongCount)
            rightGuess = multiGuessWord1(guessPool)
            singleGuessWord2()
            print("\nWrong guess!")

        elif len(pguess) >= malength:
            clear()
            print("-" * 2)
            guesser += 1
            wrongCount += 1
            wrongman(wrongCount)
            rightGuess = multiGuessWord1(guessPool)
            multiGuessWord2()
            print(f"Your guess has {len(pguess)} letters, the correct answer only has {malength} answers.")
    else:
        clear()
        print("-" * 26)
        wrongman(wrongCount)
        print(f'Player {guesser} guessed the last letter! The word is: {multiAnswer}!')
        print(f'A point for player {guesser}!')
        outro()


intro()
gamesel()
