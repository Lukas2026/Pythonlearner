player = '@'
hp = 20
px,py = 1,1
level = []
raw = '........f....g.....M..M..g..P...'
level = list(raw)
print(level)
#ask
while True:
	for x,char in enumerate(level):
		if x == px:
			print(player,end = '')
		else:
			print(char,end = '')
	print()
	command = input('>>>')
	if command == 'a':
		px -= 1
	if command == 'd':
		px += 1
