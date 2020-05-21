# Hangman game with ascii art!

import random

def randomselect(): 
    # randomly selects any word from any genre.
    wordsample = {
"anime" : ["code geass" , "steins;gate" , "kimi no na wa" , "cowboy bebop" , "zankyo no terror" , "death note" , "attack on titan"] ,
"fruits" : ["apple" , "bananna" , "grapes" , "watermelon" , "orange"] ,
"palindrome" : ["malayalam" , "noon"] ,
"quote" : ["ely psy congree" , "nunally no tasketukrae"]
}   
    wordtype = random.choice(list(wordsample.keys()))
    print("Guess the " + wordtype + " :")
    return random.choice(wordsample[wordtype])

def guessandcheck(word , l):
    # checks if the input letter is in the secreat word
    guess = input("Guess a letter: ")
    for i in range(len(word)):
        if guess == word[i] and l[i] != word[i]:
            return i
    return

def updatel(l , word , i):
    l[i] = word[i]
    print(" ".join(l))
    return 

def ascii(wrongcnt):
    # ascii art
    hangmanpics = [r"""
    +----+
    |    |
         |
         |
         |
         |
    =======""" , r"""
    +----+
    |    |
    O    |
         |
         |
         |
    =======""",r"""
    +----+
    |    |
    O    |
    |    |
         |
         |
    =======""",r"""
    +----+
    |    |
    O    |
   /|    |
         |
         |
    =======""",r"""
    +----+
    |    |
    O    |
   /|\   |
         |
         |
    =======""",r"""
    +----+
    |    |
    O    |
   /|\   |
    |    |
         |
    =======""",r"""
    +----+
    |    |
   [O]   |
   /|\   |
    |    |
         |
    ======="""]
    if wrongcnt >= len(hangmanpics):
        print("Sorry ! You have run out of maximun tries.")
        return
    else:
        return hangmanpics[wrongcnt]

def checkwin(l,word):
    final = "".join(l)
    if final == word:
        return True
    else:
        return False

def main():
    word = randomselect()
    l = []
    wrongcnt = 0 
    for ch in word:
        if ch != " ":
            l.append("_")
        else:
            l.append(" ")
    print(" ".join(l))
    print(ascii(wrongcnt))
    while "_" in l:
        ans = guessandcheck(word , l)
        if ans != None:
            print("You guessed a correct word!!")
            updatel(l,word,ans)
        else:
            print("Wrong guess :(")
            print(" ".join(l))
            wrongcnt += 1
            draw = ascii(wrongcnt)
            if draw == None:
                if input("Would you like to play again? ").lower().startswith("y"):
                    main()
                break
            else:
                print(draw)
    if checkwin(l,word) == True:
        print("Ely psy Congree!")
        if input("Would you like to play again? ").lower().startswith("y"):
            main()

main()