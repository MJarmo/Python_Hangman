import os

def playGame(data1):
    attemps = 9
    data = list(data1)
    guess = ['_']
    for i in range(len(data)-1):
        guess.append('_')
    while (attemps>0):
        letter = input("Enter Your Letter: ")
        if (letter in data):
            for j in range(len(data)):
                if (data[j] == letter):
                    guess[j] = letter
            print("Your word so far: ", *guess)
        else:
            attemps = attemps -1
            print("Ther is no " , letter , "in word")
            print(attemps-1 , " attemps left")
        if ('_' not in guess):
            print("You Won u tricky bastard, Word is: ", "".join(guess))
            return True
    print("U lost gg, word was: ", guess)

word = ()
while (True):
    print("=================================================")
    print("==================HANGMAN========================")
    print("==================THE GAME=======================")
    print("=================================================")
    print("1.Enter your word to quest")
    print("2.Start Game")
    print("3.Exit")
    menu_pick = input()

    if menu_pick == '1':
        word = input("Enter word to guess: ")
        os.system("cls")
    if menu_pick == '2':
        playGame(str(word))
    if menu_pick == '3':
        quit()