print("hello! welcome to hangman.")


def menu():
    global wordpool
    wordpool = 0
    while wordpool == 0:
        print("if you would like to use your own word file, please paste the file name below. if not, type \"D\", and the game will start with the default word pool.")
        x = input()

        if x.upper() == "D":
            try:
                file=open("words.txt")
                wordpool=file.read()
            except:
                print("default file not found")
        else:
            try:
                x = x.replace("\\", "\\\\")
                file=open(x)
                wordpool=file.read()
            except:
                print("file not found. make sure the text file is in the same folder as the program")

        wordpool = wordpool.split()

        global losingchance
        if input("would you like to turn on the possibility of losing? type \"Y\" for yes. type anything else to continue in invincible mode ").upper() == "Y":

            losingchance = True
        else:
            losingchance = False

import random

import time

games_won = 0

pronoun = ["his", "her", "their", "his", "her", "their", "its", "zir"]
family = ["father", "mother", "guardian", "wife", "husband", "partner", "best friend"]

menu()

while True:
    guesses = 0
    correctletters = []
    incorrectletters = []
    guess = 0
    word = wordpool[random.randint(0, len(wordpool) - 1)]
    while guess != word:
        losing = 0
        print("your word is ", end="")
        for i in word:
            if i in correctletters:
                print(i, end="")
            else:
                print("_", end="")
                losing += 1
        print("\n", end="")

        if losingchance:
            print("you have " + str(10 - guesses) + "/10 guesses left")
            if losing == 0 or guesses >= 10:
                break


        guess = input("enter a letter or a word \n").lower()
        if len(guess) == 1:
            if guess in correctletters:
                print("you already guessed that")
            elif guess in word:
                correctletters.append(guess)
            else:
                incorrectletters.append(guess)
                guesses += 1
                print(guess + " isn't in the word")
        else:
            guesses += 1

    if guess == word:
        print("congratulations! you guessed the word!")
        games_won += 1
        print("you have won " + str(games_won) + " games so far B)")

    if losingchance:
        if losing == 0 or guesses >= 10:
            print("you lose!")
            time.sleep(0.3)
            print("the word was \"" + word + "\"")
            time.sleep(0.3)
            print("____")
            time.sleep(0.3)
            print("|  o")
            time.sleep(0.3)
            print("| /|\\")
            time.sleep(0.3)
            print("| //")
            time.sleep(0.3)
            print("|")
            time.sleep(0.3)
        if games_won in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            print(str(games_won) + " games? thats so many!")
        if games_won == 100:
            print("you have won the game! now hangman gets to see " + random.choice(pronoun), random.choice(family))
            time.sleep(0.3)
            print("____")
            time.sleep(0.3)
            print("|  |")
            time.sleep(0.3)
            print("|            o    o    <(thank god!)")
            time.sleep(0.3)
            print("|            \\\\  //")
            time.sleep(0.3)
            print("|  ☐        /)   (\\")
            time.sleep(0.3)

    if input("if youd like to go to main menu, type \"M\". type anything else to play again. ").upper() == "M":
        menu()


