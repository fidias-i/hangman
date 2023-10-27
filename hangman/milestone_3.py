from milestone_2 import word
#print(word)
while True:
    guess = input('Enter a letter: ')
    if len(str(guess)) == 1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
     print(f"Sorry, {guess} is not in the word. Try again.")