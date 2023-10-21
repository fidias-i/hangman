import random

word_list = ['blueberry','banana','pineapple','mango','strawberry']
#print(word_list)

word  = random.choice(word_list)
#print(word)

guess = input('Enter a letter: ')
if len(str(guess)) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
#if (len(guess) == 1) and (guess.isalpha()):
#    print('Good guess!')
