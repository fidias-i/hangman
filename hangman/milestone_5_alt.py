import random
class Hangman():
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set([letter for letter in self.word]))
        self.list_of_guesses = []
        self.play_game()
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

    def play_game(self):
        while True:
            if self.num_lives == 0:
                print('You lost!')
                break
            if self.num_letters > 0:
                self.ask_for_input()
                print(self.num_lives)
                print(type(self.num_lives))
                print('\n')
                print(self.num_letters)
                print(type(self.num_letters))
            if self.num_lives != 0 and self.num_letters == 0:
                print('Congratulations. You won the game!')
                break


if __name__ == "__main__":
    game = Hangman(['apple'])