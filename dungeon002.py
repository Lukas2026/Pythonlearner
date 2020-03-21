player = '@'
hp = 20
gold = 0
food = 0
px,py,pz = 3,3,0
level1 = '''
#############################################################
#...........................................................#
#.....................................$.....................#
#...................f...............................$.......#
#...........................................................#
#.....$...........................f.........................#
#...........................................................#
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
#........................................$.......f..........#
#...........................................................#
#..........$......f.........f.......$..............f........#
#...........................................................#
#...........................................................#
############################.################################
#####################.................#######################
#####################.................#######################
#############################################################'''

#create dungeon
dungeon = []
for raw in (level1,level2):
    level = []
    for line in raw.splitlines():
        level.append(list(line))
    dungeon.append(level)
    
print(dungeon)

print(dungeon[0][2])
    
# # ..... rock
# f ...... food
# $ ....... gold
message = ''
while hp > 0:
    for y,line in enumerate(dungeon[pz]):
        for x,char in enumerate(line):
            if x == px and y == py:
                print(player, end = '')
            else:
                print(char,end = '')
        print()
    print(message)
    command = input('{} hp, {} $, {} f >>>'.format(hp,gold,food))
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
        pz -= 1
        if pz < 0:
            pz = 0
    if command == 'climb down':
        pz += 1
        if pz > len(dungeon) -1:
            pz = len(dungeon) -1
    #check ob in felsen
    target = dungeon[pz][py + deltay][px + deltax]
    if target == '#':
        message += 'ouch'
        hp -= 1
        deltax = 0
        deltay = 0
       
    #movement
    px += deltax
    py += deltay
    #picking up itmes
    target = dungeon[pz][py][px]
    if target == '$':
        message += 'You found Gold!'
        gold += 1
        dungeon[pz][py][px] = '.'
    if target == 'f':
        message += 'You Found Food'
        food += 1
        dungeon[pz][py][px] = '.'
        
        
        


print('Game over')
    
