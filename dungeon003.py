import random
class Game:
    zoo = {}
    
class Monster:
    number = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.char = "M"
        print('A new monster has been created')
        self.number = Monster.number
        Monster.number += 1
        Game.zoo[self.number] = self # put monster in zoo
        self.hp = random.randint(50, 80)
        self.attack  = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.damage = random.randint(1, 6)
        
    def __str__(self):
        return "I am Monster Number #{} my stats are: {} hp, {} att, {} def, {} dam".format(self.number, self.hp, self.attack, self.defense, self.damage)

# Player is a child class of Monster

class Player(Monster):
    
    def __init__(self, x, y, z):
        super().__init__(x,y,z) # calls the parent class
        self.char = "@"
        self.hp = random.randint(150,200)
        self.attack += 6
        self.defense += 6
        self.gold = 0
        self.food = 0
       

#build 10 monsters
#for _ in range(10):
#    Monster()
    
#for m in Game.zoo.values():
    #print(m)

player = Player(3,3,0)

level1 = '''
#############################################################
#...........................................................#
#..............M......................$.....................#
#...................f...............................$.......#
#...........................................................#
#.....$...........................f.........................#
#..............M............................................#
#............f.......................................f......#
#...........................f.........$.....................#
#...........................................................#
#############################################################'''
level2 = '''
#############################################################
#...........................................................#
#........................................f.............$....#
#.......$.......f..............$............................#
#...........................................................#
#...........M............................$.......f..........#
#...........................................................#
#..........$......f.........f.......$..............f........#
#............M....M.........................................#
#...........................................................#
############################.################################
#####################.................#######################
#####################.................#######################
#############################################################'''

#create dungeon
dungeon = []
for z, raw in enumerate((level1,level2)):
    level = []
    for y, raw_line in enumerate(raw.splitlines()):
        line = []
        for x, char in enumerate(raw_line):
            if char=="M":
                Monster(x,y,z)
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
while player.hp > 0:
    for y,line in enumerate(dungeon[player.z]):
        for x,char in enumerate(line):
            # Monster here ?
            for m in Game.zoo.values():
                if m.z == player.z and m.y == y and m.x == x and m.hp > 0:
                    print(m.char, end="")
                    break
            else:
                print(char, end="")
        print()
    print(message)
    command = input('{} hp, {} $, {} f >>>'.format(player.hp,player.gold,player.food))
    message = ''
    deltax = 0 #wo der spieler gehen will
    deltay = 0
    if command == 'a':
        deltax = -1
    if command == 'd':
        deltax = 1
    if command == 'w':
        deltay = -1 #y achse lauft nach unten
    if command == 's':
        deltay = 1
    #change level
    if command == 'climb up':
        player.z -= 1
        if player.z < 0:
            player.z = 0
    if command == 'climb down':
        player.z += 1
        if player.z > len(dungeon) -1:
            player.z = len(dungeon) -1
    #check ob in felsen
    target = dungeon[player.z][player.y + deltay][player.x + deltax]
    if target == '#':
        message += 'ouch'
        player.hp -= 1
        deltax = 0
        deltay = 0
    # check if running into Monster    
    for m in [m for m in Game.zoo.values() if m.hp>0 and
              m.number != player.number and m.z == player.z and 
              m.y == player.y + deltay and m.x == player.x + deltax]:
        message += "attacking Monster!"
        deltax, deltay = 0, 0 # player stop moving
        #break
    #movement
    player.x += deltax
    player.y += deltay
    #picking up itmes
    target = dungeon[player.z][player.y][player.x]
    if target == '$':
        message += 'You found Gold!'
        player.gold += 1
        dungeon[player.z][player.y][player.x] = '.'
    if target == 'f':
        message += 'You Found Food'
        playre.food += 1
        dungeon[player.z][player.y][player.x] = '.'
        
        
        


print('Game over')
    
