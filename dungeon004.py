import random
import os
def roll2(number, sides, reroll):
    result = random.randint(1, sides)
    if reroll and result == sides:
        total += result -1 + roll2(sides,reroll)
    else:
        total += result
    return total
    
def roll(die):
    '''return integer value from dice roll'''
    if "D" in die:
        reroll = True
    else:
        reroll = False
    number = int(die.lower().split('d')[0])
    sides = int(die.lower().split('d')[1])
    total = 0
    for i in range(number):
        total += roll2(sides, reroll)
    return total


def strike(attacker, defender, counter=False):
    '''attacking monster strikes a defending monster'''
    a = attacker.attack()
    b = defender.defense()
    c = attacker.damage()
    text = '{} {} strikes at {} with {} vs {}: '.format(attacker.__class__.__name__,
                                                        'counter' if counter else '', defender.__class__.__name__, a, b)
    if a > b:
        text += 'HIT with {} damage'.format(c)
        defender.hp -= c
        text += ' ({} hp left)'.format(defender.hp)
    else:
        text += 'MISS'
    return text


def fight(attacker, defender):
    '''strike and counter strike'''
    text = strike(attacker, defender)
    if defender.hp > 0:
        text += '\n' + strike(defender, attacker, True)
    return text


class Game:
    zoo = {}


class Monster:
    number = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dx = 0
        self.dy = 0
        self.char = "M"
        print('A new monster has been created')
        self.number = Monster.number
        Monster.number += 1
        Game.zoo[self.number] = self  # put monster in zoo
        self.hp = random.randint(50, 80)
        self.attackroll = '1d6'
        self.defenseroll = '1d6'
        self.damageroll = '1d6'
    def ai(self):
        player = Game.zoo[0]
        self.detectionradius = 7
        distance = ((self.x - player.x) + (self.y + player.y))**0.5
        self.dx, self.dy = 0, 0
        if distance > self.detectionradius:
            #monster can not sniff player
            self.dx = random.choice((-1,0,0,1))
            self.dy = random.choice((-1,0,0,1))
        else:
            if player.x > self.x:
                self.dx = 1
            elif player.x < self.x:
                self.dx = -1
            if player.y > self.y:
                self.dy = 1
            elif player.y < self.y:
                self.dy = -1
                
    def attack(self):
        return roll(self.attackroll)

    def defense(self):
        return roll(self.defenseroll)

    def damage(self):
        return roll(self.damageroll)

    def __str__(self):
        return self.__class__.__name__ + ':' + str(self.__dict__)

        # return "I am Monster Number #{} my stats are: {} hp, {} att, {} def, {} dam".format(self.number, self.hp, self.attack, self.defense, self.damage)


# Player is a child class of Monster

class Player(Monster):

    def __init__(self, x, y, z):
        super().__init__(x, y, z)  # calls the parent class
        self.char = "@"
        self.hp = random.randint(150, 200)
        self.attackroll = '2d6'
        self.defenseroll = '2d4'
        self.damageroll = '1d10'
        self.gold = 0
        self.food = 0
        self.saturation = 1  # 100% = 1.0 50% = 0.5 etc.


# build 10 monsters
# for _ in range(10):
#    Monster()

# for m in Game.zoo.values():
# print(m)

player = Player(3, 3, 0)

# ---------- importing level001.txt, level002.txt
# ---- eine level datei muß heißen "level" dann eine nummer, und dann Endung ".txt"
level_list = []

for root, dirs, files in os.walk("."):
    for file in sorted(files):
        if file[:5] == "level" and file[-4:] == ".txt":
            print("reading from disk" , file)
            with open(file) as f:
                lines = f.readlines()
                level_list.append(lines)


# create dungeon
dungeon = []
for z, raw in enumerate(level_list):
    level = []
    for y, raw_line in enumerate(raw):
        line = []
        for x, char in enumerate(raw_line.strip()):
            if char == "M":
                Monster(x, y, z)
                line.append(".")
            else:
                line.append(char)

        level.append(line)
    dungeon.append(level)

# # ..... rock
# f ...... food
# $ ....... gold
# M ....... Monster
message = ''
while player.hp > 0 and player.saturation > 0:
    #------ monster movement --- 
    for m in [m for m in Game.zoo.values() if m.number != 0 and m.z == player.z and m.hp > 0]:
        m.ai()
        target = dungeon[m.z][m.y+m.dy][m.x+m.dx]
        if target == "#" :
            m.dx, m.dy = 0, 0
        for m2 in [m for m in Game.zoo.values() if m.z==player.z and m.hp > 0]:
            if m2.number == m.number:
                continue
            if m2.x == m.x + m.dx and  m2.y == m.y + m.dy:
                m.dx, m.dy = 0, 0
                if m2.number == 0:
                    message += fight(m, player)
                break
        else:
            m.x += m.dx
            m.y += m.dy
    #----- grafical engine -----
    for y, line in enumerate(dungeon[player.z]):
        for x, char in enumerate(line):
            # Monster here ?
            for m in Game.zoo.values():
                if m.z == player.z and m.y == y and m.x == x and m.hp > 0:
                    print(m.char, end="")
                    break
            else:
                print(char, end="")
        print()
    print(message)
    command = input(
        '{} hp,{:.0f}% saturation, {} $, {} f >>>'.format(player.hp, player.saturation * 100, player.gold, player.food))
    message = ''
    # speical commands
    if command.lower() == 'quit' or command.lower() == 'exit':
        break
    if command.lower() == 'eat':
        if player.food < 1:
            message += 'You have no food'
        else:
            player.saturation += 0.3
            player.food -= 1
            message += 'YUM'
    deltax = 0  # wo der spieler gehen will
    deltay = 0
    if command == 'a':
        deltax = -1
    if command == 'd':
        deltax = 1
    if command == 'w':
        deltay = -1  # y achse lauft nach unten
    if command == 's':
        deltay = 1
    # change level
    if command == 'climb up':
        player.z -= 1
        if player.z < 0:
            player.z = 0
    if command == 'climb down':
        player.z += 1
        if player.z > len(dungeon) - 1:
            player.z = len(dungeon) - 1
    # check ob in felsen
    target = dungeon[player.z][player.y + deltay][player.x + deltax]
    if target == '#':
        message += 'ouch'
        player.hp -= 1
        deltax = 0
        deltay = 0
    # check if running into Monster
    for m in [m for m in Game.zoo.values() if m.hp > 0 and
                                              m.number != player.number and m.z == player.z and
                                              m.y == player.y + deltay and m.x == player.x + deltax]:
        # message += "attacking "+ str(m)
        message += fight(player, m)
        deltax, deltay = 0, 0  # player stop moving
        # break
    # movement
    player.x += deltax
    player.y += deltay
    # hunger
    player.saturation -= 0.01

    # picking up itmes
    target = dungeon[player.z][player.y][player.x]
    if target == '$':
        message += 'You found Gold!'
        player.gold += 1
        dungeon[player.z][player.y][player.x] = '.'
    if target == 'f':
        message += 'You Found Food'
        player.food += 1
        dungeon[player.z][player.y][player.x] = '.'

print('Game over')
if player.hp < 1:
    print('You lost all your hp')
elif player.saturation <= 0:
    print('You died of hunger')
else:
    print('You quit the game')

