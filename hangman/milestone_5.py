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
            for idx,letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[idx] = letter
            self.num_letters -= 1
        else:
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
    def ask_for_input(self):
        self.guess = input('Enter a letter: ')
        if len(str(self.guess)) != 1 and self.guess.isalpha() == False :
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif self.guess in self.list_of_guesses:
            print('You have already tried that letter!')
        else:
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)




def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        if game.num_letters >0:
            game.ask_for_input()
            print(game.num_lives)
            print(type(game.num_lives))
            print('\n')
            print(game.num_letters)
            print(type(game.num_letters))
        if game.num_lives !=0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

play_game(['apple'])