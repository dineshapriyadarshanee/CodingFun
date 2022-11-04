# Name: Dinesha Priyadarshanee 

# Import the necessary modules.
import enchant # Used to import pyenchant package.
import json # Used to convert between JSON-formatted text and Python variables.
import string # Used to provide convenient access to a string variable containing all uppercase letters.
import random # Used to randomly select letters.
from os import path # Used to find the path of the file.

#Dictionary which contains the score values for each letters in the alphabet.
dict_weights = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 'D':2, 'G':2,
                         'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8,
                         'Q':10, 'Z':10}

# This function generates and returns a list of 9 letters.
def select_letters():
    # This tuple contains 26 numbers, representing the frequency of each letter of the alphabet in Scrabble.
    letter_weights = (9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1)

    # The letter_weights tuple is used in this call to the "random.choices()" function, along with
    # the pre-defined "string.ascii_uppercase" variable which contains the letters A to Z.
    chosen_letters = random.choices(string.ascii_uppercase, weights=letter_weights, k=9)

    # Returning the created list of 9 random letters using the specified letter frequencies.
    return chosen_letters

# This function displays the 9 letters in a 3x3 grid.
def display_letters(letters):
    i = 0
    length = len(letters)
    
    while i < length:
        print((str(' '+ letters[i]+ ' | '+ letters[i+1]+ ' | '+ letters[i+2])).center(50))#printing 3 letters in a row seperated by '|'
        i += 3
        if i < length:
            print(('-'*11).center(52))#placing 11 '-' marks.

#This function displays the words saved in the list.
def display_words(words):
    if len(words) == 0:
        print('You have not yet entered any words.')
    else:
        print('Previously entered words:')
        words.sort()
        for word in words:
            print('- ', word)

# This function checks whether a word entered by the user contains appropriate letters.
def validate_word(word, letters):
    temp = letters.copy()
    for letter in word:        
        if not (letter in temp):
            return False
        else:
            temp.remove(letter)# Used letters are removed to check whether the user trys the same letter twice.

    # Checking whether the word is a valid English word.
    dic = enchant.Dict('en_US')
    return dic.check(word)

# This function returns the score for a given word.
def request_scrabble_score(user_input):
    score = 0
    for letter in user_input:
        score += dict_weights.get(letter)

    return score

# This function is used to log the data including given letters, user given words and the score of different rounds.
def log_data(letters, used_words, score):    
    file_name = 'log.txt'
    dict_log = {'letters': letters, 'words': used_words, 'score': score}
    saved_list = []

    #Checking whether the file is available in the current directory.
    if path.isfile(file_name) is True:
        #Open the file in read mode and load the content written in json format.
        with open(file_name, 'r') as fp:
           listObj = json.load(fp)
           for obj in listObj:
               #Save the logs inside a list.
               saved_list.append(obj)
           fp.close()        

    #Add the current game's data to the same list.
    saved_list.append(dict_log)
    
    #Open the file again and write the data saved in the list.
    with open(file_name, 'w') as f:
        json.dump(saved_list, f, ensure_ascii=False, sort_keys=False, indent=4, skipkeys = True)       

# Welcome the user and create necessary variables.
print('Welcome to Word Find.')
print('Come up with as many words as possible from the letters below!', '\n')

hard_mode = False
score = 0
used_words = []
letters = select_letters()#Letters are selected randomly and saved in a variable.

# Ask the user to select easy mode or hard mode.
while True:
    mode = (input('Do you wish to play [e]asy mode or [h]ard mode?')).upper()
    
    #Validation for the mode to check whether the user input is invalid.
    if mode == 'E':
        print('Easy mode selected.\n')
        hard_mode = False
        break
    elif mode == 'H':
        print('Hard mode selected. Entering an invalid word will end the game!\n')
        hard_mode = True
        break
    else:
        print('Invalid input, please select a mode.\n')


# Enter gameplay loop.
while True:
    # Display score, letter grid and prompt user for input.
    print('Score: ', score, '. Your letters are: \n')
    display_letters(letters)
    
    user_input = (input('Enter a word, [s]huffle letters, [l]ist words, or [e]nd game:')).upper()
    
    if user_input == 'E':#If user enters 'E', end the game.
        print('Ending the game...')
        break    
    elif user_input == 'S':#If user enters 'S', shuffle the letters
        random.shuffle(letters)
        print('Shuffling letters...\n')
    elif user_input == 'L':#List previously entered words
        display_words(used_words)
    elif len(user_input) < 3:#If user has entered a word with less than 3 characters, it is considered as invalid.
        print('The word is invalid. Too short word.')
        if hard_mode:
            print('Game Over!')
            break        
    elif user_input in used_words:#User has entered a word already entered before.
        print('Word already exists in the list.')
        if hard_mode:
            print('Game Over!')
            break
    elif validate_word(user_input, letters):#Validation for the given word is checked here.
        sc = request_scrabble_score(user_input)#If a valid word is given, the score is calculated.
        print('Word accepted. Score for the word is :' , sc)
        score += sc
        used_words.append(user_input)
    else:
        print('Invalid word entered.')
        if hard_mode:
            print('Game Over!')
            break
        
print('Your final score is : ', score)

if score > 50:
    print('Congratulations! You have earned a good score.')
    #Loging data including letters, words and score in a file named 'log.txt' in json format.
    log_data(letters, used_words, score)

print('Thank you for playing!')        
    


    
