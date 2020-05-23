animals = {}
with open('animal2.csv') as f:
    lines = f.readlines()
#file closed
line0 = lines[0]
#print(line0.split(','))
spalten = [name.strip() for name in line0.split(',')]
print(spalten)
fields = [name.strip() for name in spalten if name not in ('','')]
print(fields)

for nr,line in enumerate(lines):
    if nr == 0:
        continue
    data = line.split(',')
    print(data)
    print(line)
    animals[data[0]] = {}
    for s in range(1,34):
        try:
            animals[data[0]][fields[s]] = bool(int(data[s].strip()))
        except:
            pass

   # if nr > 5:
   #     break
print(animals)
print(animals['Dog']['mammal'])