import random
print(
    '''
Welcome to password maker!!!! this program ask you simple questions
and then creates a password out of your answers
'''
    )
word = input('What word would you like to use?   :')
simbols = input('what simbols would you like to use?   :')
numbers = input('what numbers would you like to use?   :')


randintnumbers = random.choice(numbers)
randintsimbols = random.choice(simbols)

password = ''
password += word
password += randintsimbols
password += randintnumbers
print(password)


