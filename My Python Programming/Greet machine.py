print('AI : What is your name?')
name = input('You:')

    

def greet(name):
	print("AI: Hello",name)

greet(name)
print('How are you doing?')
How_are_you_doing = input('You:')

if 'about you' in How_are_you_doing:
    print('AI: Good, I finaly have someone to talk to!!')
elif 'bad' or 'Bad' in How_are_you_doing:
        print('AI: What happend?')
        badstuff = input('You:')
else:
    print('AI: Me too')




if 'e' or 'i' or 'o' or 'a' or 'u' or 'y' or 'E' or 'I' or 'O' or 'A' or 'U' or 'Y' in badstuff:
        print('I am sorry to hear so :(')
        
