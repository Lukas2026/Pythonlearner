print(
    '''
    Choose one:
    '''
)
print(
    '''
    Fresh Crab
    Hippo
    Butterfly
    Pigeon
    Coyote
    Antelope
    Owl
    Koala
    Gorilla
    Reindeer
    Cheetah
    Cougar
    Goat
    Racoon
    Domestic Pig
    Duck
    Ant
    Hare
    Chicken 
    Penguins
    Crocodiles
    Polar Bear
    Squirrels
    Lizard
    Spider
    Leopard
    Giraffe
    Turtle
    Giant Panda
    Rhino
    Cattle
    Horse
    Frog
    Bat
    Shark
    Wolf
    Tiger
    Snake
    Deer
    Lion
    Bear
    Cat 
    Dog
    '''
)
print(
    """
    Now I will guess whatever animal you choose by asking you a few questions:
    
    Please write Y/N as an answer
"""

)
vertabreate = input('Is your animal a vertibreate? ')
if vertabreate == 'Y':
    mammal = input('Is your animal a mammal? ')
    if mammal == 'Y':
        carnivore = input('Is your animal a carnivore? ')
        if carnivore == 'Y':
            catkind = input('Is your animal some sort of cat kind? ')
            if catkind == 'Y':
                native_to_africa = input('Is your animal native to africa? ')
                if native_to_africa == 'Y':
                    dots = input('Does your animal have dots on its fur? ')
                    if dots == 'Y':
                        fastest = input('Is your animal considered fastest on land? ')
                        if fastest == 'Y':
                            print('Your animal is a Cheetah!')
                        else:
                            print('Your animal is a Leopard!')
                    else:
                        print('Your animal is a lion')
                else:
                    pet = input('Is your animal a Pet? ')
                    if pet == 'Y':
                        print('Your animal is a Cat')
                    else:
                        native_to_canada = input('Is your animal native to canada? ')
                        if native_to_canada == 'Y':
                            print('Your animal is a cougar')
                        else:
                            print('Your animal is a Tiger')
            else:
                forest = input('Can you find your animal in a forest? (Not water) ')
                if forest == 'Y':
                    large = input('Is your animal considered big? (Wolves arent) ')
                    if large == 'Y':
                        print('Your animal is a Bear/Polar Bear')
                    else:
                        wolf = input('Is your animal considered the ansestor of the dog? (Coyotes arent) ')
                        if wolf == 'Y':
                            print('Your animal is a Wolf')
                        else:
                            print('Your animal is a Coyote')




        else:
            omnivore = input('Is your animal an omnivore? ')
            if omnivore == 'Y':
                pet_domestic = input('Is your animal a Pet or is it Domestic? ')
                if pet_domestic == 'Y':
                    pet = input('Is your animal a Pet? ')
                    if pet == 'Y':
                        print('Your animal is a dog')
                    else:
                        print('Your animal is a Pig (Domestic)')
                else:
                    large = input('Is your animal considered big? ')
                    if large == 'Y':
                        water = input('Does your animal live in water? ')
                        if water == 'Y':
                            print('Your animal is a Hippo')
                        else:
                            print('Your animal is a Giant Panda')
                    else:
                        print('Your animal is a Racoon')
            else:
                herbevore = input('Is your animal a herbevore? ')
                if herbevore == 'Y':
                    horns = input('Does your animal have horns? (Cattle inclueded)')
                    if horns == 'Y':
                        farm = input('Is your animal a farm animal?')
                        if farm == 'Y':
                            cow = input('Is your animal similar to a cow? (Goat is not)')
                            if cow == 'Y':
                                print('Your animal is a cattle')
                            else:
                                print('Your animal is a Goat')
                        else:
                            native_to_africa = input('Is your animal native to africa? ')
                            if native_to_africa == 'Y':
                                fast = input('Is your animal quite fast? ')
                                if fast == 'Y':
                                    print('Your animal is an antelope')
                                else:
                                    print('Your animal is a Rhino')
                            else:
                                cold = input('Is your animal adapted to cold climate? (Deer is not Reindeer is) ')
                                if cold == 'Y':
                                    print('Your animal is a Reindeer')
                                else:
                                    print('Your animal is a Deer')
                    else:
                        trees = input('Does your animal live in the trees? ')
                        if trees == 'Y':
                            ape = input('Is your animal some sort of ape? ')
                            if ape == 'Y':
                                print('Your animal is a gorilla')
                            else:
                                native_to_australia = input('Is your animal native to australia? ')
                                if native_to_australia == 'Y':
                                    print('Your animal is a Koala')
                                else:
                                    print('Your animal is a squriell')
                        else:
                            native_to_africa = input('Is your animal native to africa? ')
                            if native_to_africa == 'Y':
                                print('Your animal is a Giraffe')
                            else:
                                large = input('Is your animal considered big? ')
                                if large == 'Y':
                                    print('Your animal is a Horse')
                                else:
                                    print('Your animal is a Hare')

                else:
                    print('WTF!!!')

    else:
        bird = input('Is your animal a Bird? (Penguins are) ')
        if bird == 'Y':
            fly = input('Can your animal fly longer than a chicken? (Ducks can) ')
            if fly == 'Y':
                eat = input('Do we eat your animal normally? ')
                if eat == 'Y':
                    print('Your animal is a duck')
                else:
                    nocturnal = input('Is your animal nocturnal? ')
                    if nocturnal == 'Y':
                        print('Your animal is an Owl')
                    else:
                        print('Your animal is a Pigeon')
            else:
                fly_ = input('Can your animal fly (Chickens can) ')
                if fly_ == 'Y':
                    print('Your animal is a Chicken')
                else:
                    print('Your animal is a Penguin')
        else:
            kill_human = input('Can your animal kill a human? ')
            if kill_human == 'Y':
                water = input('Does your animal live in water? ')
                if water == 'Y':
                    reptile = input('Is your animal a reptile? ')
                    if reptile == 'Y':
                        print('Your animal is a Crocodile')
                    else:
                        print('Your animal is a shark')
                else:
                    print('Your animal is a snake')

            else:
                water_ = input('Does your animal sometimes go in water? (Lizards dont) ')
                if water_ == 'Y':
                    print('Your animal is a Turtle')
                else:
                    print('Your animal is a Lizard')

elif vertabreate == 'N':
    insect = input('Is your animal an insect? (Spiders are not insects) ')
    if insect == 'Y':
        fly = input('Can your animal fly? ')
        if fly == 'Y':
            print('Your animal is a Butterfly')
        else:
            print('Your animal is an ant')
    else:
        water = input('Does your animal live in water? ')
        if water == 'Y':
            print('Your animal is a fresh crab')
        else:
            print('Your animal is a spider')




