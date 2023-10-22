import random
class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set([letter for letter in self.word]))
        self.list_of_guesses = []

    def check_guess(self,guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")
        else:
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
    def ask_for_input(self):
        while True:
            self.guess = input('Enter a letter: ')
            if len(str(self.guess)) != 1 and self.guess.isalpha() == False :
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif self.guess in self.list_of_guesses:
                print('You have already tried that letter!')
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)

game = Hangman(['apple'])
game.ask_for_input()