import PySimpleGUI as sg

def read_animal_file():
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


    #print(animals['Dog']['mammal'])
    return animals


animals = read_animal_file()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()