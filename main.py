# HANGMAN
import random
import time


def welcome():
    print('Welcome to Hangman!')
    time.sleep(.5)
    print('To get started, let\'s first choose a category. Your options are . . .')
    time.sleep(.5)
    # Block below could be put in for loop if there were many more options
    print('OPTION 1: weather')
    time.sleep(.5)
    print('OPTION 2: animals')
    time.sleep(.5)
    print('OPTION 3: drinks')


def play_again():
    quit()


def get_word():
    weather_words = ['sunny', 'rainy', 'cloudy', 'thundering', 'breezy', 'wintry', 'squalling', 'sprinkling']
    animal_words = ['poodle', 'zebra', 'elk', 'ocelot', 'condor', 'butterfly', 'gecko', 'rhinoceros']
    drink_words = ['chai', 'coke', 'rootbeer', 'water', 'lemonade', 'coffee', 'milk', 'sprite', 'juice']

    word = None
    cat = input('Which option would you like? : ').lower()
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

    welcome()
    word = get_word()





play_game()

