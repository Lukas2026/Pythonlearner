player = '@'
hp = 20
px,py = 1,1
level = []
# # ..... rock
# f ...... food
# g ....... gold
raw = '#.......f....g.....M..M..g..P..#'
level = list(raw)
print(level)
while hp > 0:
    for x,char in enumerate(level):
        if x == px:
            print(player,end = '')
        else:
            print(char,end = '')
    print()
    command = input('>>>')
    deltax = 0 #wo der spieler gehen will
    if command == 'a':
        deltax = -1
    if command == 'd':
        deltax = 1
    #check ob in felsen
    target = level[px + deltax]
    if target == '#':
        print('ouch!')
        hp -= 1
        print('you have',hp,'hitpoints')
        deltax = 0
       
    #movement
    px += deltax
print('Game over')
