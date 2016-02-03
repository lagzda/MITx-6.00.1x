# A helper function that checks if the word is guessed
def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

# A helper function that returns the guessed letters of the word
def getGuessedWord(secretWord, lettersGuessed):
    word = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter + " "
        else:
            word += "_ "
    return word 

# A helper function to print out all available letters to guess
def getAvailableLetters(lettersGuessed):
    available_letters = ""
    for index in range(97, 123):
        if chr(index) not in lettersGuessed:
            available_letters += chr(index)
    return available_letters

def hangman(secretWord):
    # Initialise lives, guessed letters and welcome the player
    lettersGuessed = []
    guesses_left = 8
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is %i letters long" % len(secretWord)
    while (True):
        # Divider
        print "-----------"
        # Check for win of loss in the game and if one is true break out of loop - Game Over
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break 
        if guesses_left <= 0:
            print "Sorry, you ran out of guesses. The word was %s" % secretWord
            break
        # Every turn notify how many guesses are left and what are the available letters    
        print "You have %i guesses left." % guesses_left
        print "Available letters: %s" % getAvailableLetters(lettersGuessed) 
        guess = raw_input("Please guess a letter: ").lower()
        # Prevent user caused errors like entered numbers or more than one letter entered or if the letter has already been guessed
        if len(guess) != 1 or not guess.isalpha():
            print "Please only enter a single alphabetic character"
            continue    
        elif guess in lettersGuessed:
            print "Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed)
            continue
        else:
            # If everything is ok then append the guess to guessed letters and check if the guess is correct
            lettersGuessed.append(guess)
            if guess in secretWord:
                print "Good guess: %s" % getGuessedWord(secretWord, lettersGuessed)
            else:
                print "Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed)
                guesses_left -= 1
                
# Test
hangman("bamba")