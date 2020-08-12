MAXWRONG = 6
print ('Welcome to Guess my Number')
print ('i am thing of a number inbetween 1 and 100')
print ('Guess it in the most least attemps posible')

import random

the_number = random.randint(1, 100)
guess = int(input('Take a guess'))
tries = 1

while guess != the_number:
    if guess > the_number:
        print ('Lower.....')
    else:
        print ('Higher......')


    guess = int(input('Take a guess'))
    tries += 1

    if tries == MAXWRONG:
        print('you lost and you suck get rekt')
        exit()


print (' You guessed it! Congratulations! the Number was', the_number)
print ("And it only took you", tries)
print ('tries')
input ('Press the enter key to exit.')
