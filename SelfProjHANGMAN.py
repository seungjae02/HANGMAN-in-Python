import random
from words import words
guessed = []

def get_word():
    randomword = random.choice(words)  # randomly chooses something from the list
    while '-' in randomword or ' ' in randomword:
        randomeword = random.choice(words)
    return(randomword)

def play():
    print("Let's play hangman!")
    word = get_word().upper()
    print(word) # For testing purposes only
    word_completion = '-' * len(word)
    tries = 6
    display_hangman(tries)
    print("What you've got so far: ", word_completion, "\n")
    while tries > 0:
        guess = input('>>> Guess a letter: ').upper()
        if len(guess) == 1 and guess.isalpha:
            if guess in guessed:
                print("\ndYou have already entered that letter. Please choose a different letter.\n")
            elif guess in word:
                guess_input = [(k,v) for (k,v) in enumerate(word) if guess == v] #guess input represents the letters that will be put in after guessing correctl
                string_list = list(word_completion) #temporary list to add the correctly guessed letters
                for k,v in guess_input: # THIS PART WAS VERY CHALLENGING
                    string_list[k] = v
                    word_completion = "".join(string_list)
                guessed.append(guess)
                if word_completion != word:
                    display_hangman(tries)
                    print("You have guessed a correct letter!")
                    print("What you've got so far: ", word_completion)
                    print("You still have", tries, "tries left. Keep going!\n")
                elif word_completion == word:
                    display_hangman(tries)
                    print("Congrats! You have guessed the word, which was", word, "\n")
                    break

            elif guess not in word:
                guessed.append(guess)
                tries -= 1
                display_hangman(tries)
                print("What you've got so far: ", word_completion)
                if tries > 0:
                    print("Sorry. That letter is not in the word. Please try again.\n")
                    print("Now you have", tries, "tries left. Good luck!\n")
                elif tries == 0:
                    print("You ran out of tries and you lost the game!\n")

        else:
            print('Not a valid input. Please try again.\n')


    askNewGame()

def askNewGame():
    while True:
        askreplay = input('Would you like to play again? Input "y" for YES or "n" for NO: ')
        if askreplay == 'y':
            print("Alright! Let's play agian!\n")
            guessed.clear()
            break
        elif askreplay == 'n':
            print("Thanks for playing! Have a good one.")
            quit()
        else:
            print('Not a valid input. Type either "y" or "n"')
            continue
    play()

def display_hangman(tries):
    stages = ["""
            __________
            |        |
            |        O
            |       \\|/
            |        |
            |       / \\
            -
            """,
            """
               __________
               |        |
               |        O
               |       \\|
               |        |
               |       / \\
               -
            """,
            """
               __________
               |        |
               |        O
               |        |
               |        |
               |       / \\
               -
            """,
            """
               __________
               |        |
               |        O
               |        |
               |        |
               |       / 
               -
            """,
            """
               __________
               |        |
               |        O
               |        |
               |        |
               |        
               -               
            """,
            """
               __________
               |        |
               |        O
               |       
               |        
               |       
               -             
            """,
            """
               __________
               |        |
               |        
               |       
               |        
               |       
               -             
            """
              ]
    print(stages[tries])

get_word()
play()



