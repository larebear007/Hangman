# HANGMAN
import random
import time


def welcome():
    print('Welcome to Hangman!')
    time.sleep(.5)
    print('To get started, let\'s first choose a category. Your options are . . .')
    time.sleep(.5)


def play_again():
    restart = input('\nThat was fun! Would you like to play Hangman again? (yes or no)')
    re = restart.lower()
    if re == 'yes' or re == 'y':
        play_game()
    else:
        print('Thanks for playing. Come again any time :)')
        quit()


def get_word():
    weather_words = ['sunny', 'rainy', 'cloudy', 'thundering', 'breezy', 'wintry', 'squalling', 'sprinkling']
    animal_words = ['poodle', 'zebra', 'elk', 'ocelot', 'condor', 'butterfly', 'gecko', 'rhinoceros']
    drink_words = ['chai', 'coke', 'rootbeer', 'water', 'lemonade', 'coffee', 'milk', 'sprite', 'juice']

    # options
    print('OPTION 1: weather')
    time.sleep(.5)
    print('OPTION 2: animals')
    time.sleep(.5)
    print('OPTION 3: drinks')
    cat = input('Which option would you like? : ').lower()

    # random word assignment
    word = None
    while True:
        if cat == 'weather':
            word = random.choice(weather_words)
            print('\nChosen Category: WEATHER \n(Guess letters for a word used to describe the weather)')
            break
        elif cat == 'animals' or cat == 'animal':
            word = random.choice(animal_words)
            print('\nChosen Category: ANIMALS \n(Guess letters for a word that is an animal)')
            break
        elif cat == 'drinks' or cat == 'drink':
            word = random.choice(drink_words)
            print('\nChosen Category: DRINKS \n(Guess letters for a word that is a type of drink)')
            break
        else:
            print('Hmm I didn\'t understand that choice. Please type "weather", "animals" or "drinks" \
            as your category choice. ')
            continue

    return word


def play_game():

    word = get_word()

    x = len(word)
    blanks = ['_'] * x
    tries = -1
    while True:
        # record of word
        print(word)
        print('\n' + ''.join(blanks))

        # finished guessing
        if ''.join(blanks) == word:
            print('YOU GUESSED THE WORD! \nYOU WIN! \nThe word was:', word)
            break

        # tries left
        tries += 1
        if tries <= 7: print('You have', 7 - tries, 'tries remaining.')
        else:
            print('Oh no, you are all out of tries! YOU LOSE! \nThe word was:', word)
            break

        # user input
        entry = input('Guess a letter or the word: ')

        # user guesses one letter
        if len(entry) == 1:
            if entry in word:
                print('Great job! That letter is in the word.')
                # REMOVED IF/ELSE HERE: see testing (1)
                idx = 0
                for letter in word:
                    if letter == entry:
                        print('Found same letter at index:', idx)
                        blanks[idx] = entry
                    idx += 1
            else:
                print('No good. That letter is not in the word.')

        # user guesses whole word
        elif len(entry) > 1:
            if entry == word:
                print('YOU GUESSED THE WORD! YOU WIN!\nThe word was:', word)
                break
            else:
                print('No good. That was not the mystery word.')

        # user entry error/ blank entry
        else:
            print('Input error: Please enter one letter.')



        # user guesses whole word
        # if entry == word:
        #     print('You guessed the word! \nYOU WIN! \nThe word was:', word)
        # else:
        #     print('Sorry that is not the word.')


    play_again()



welcome()
play_game()

