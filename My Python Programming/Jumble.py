import random
WORDS = ('python', 'programing', 'handkerchief', 'difficult', 'xylophone', 'electricity')
word = random.choice(WORDS)
correct = word
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]


print(
    '''


               Welcome to the game jumble!


            Unscrable the letters to make a word.
         (press the enter key at the promt to quit)
'''

)
print('the jumble is',jumble)

guess = input('Your guess: ')

while guess != correct and guess != '' and guess != 'HINT':
    print ('sorry but that is not it :(')
    guess = input('Your guess: ')

if guess == correct:
    print('that is it! you guessed it')
    print('thanks for playing')
    input('Press the enter key to exit')
    
    
