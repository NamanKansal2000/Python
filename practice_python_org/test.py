print("Welcome to Hangman!")
word = "EVAPORATE"

guessed = '_'*len(word)
word = list(word)
guessed = list(guessed)
lst_guessed = []
letter = input("Guess letter: ")
while True:
    if letter in lstGuessed:
        letter = ""
        print("Already guessed! ")

    elif letter in word:
        index = word.index(letter)
        guessed[index] = letter
        word[index] = '_'
