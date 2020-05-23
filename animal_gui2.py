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
    return animals, fields


animals, fields = read_animal_file()

#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
#[sg.Text('Animal:'),sg.Combo(tuple(animals.keys()),key = 'animal'),
#                               sg.Combo(fields,key = 'attribute')],


#[sg.Checkbox('My Checkbox', "RADIO2",key = 'Check1'),
#              sg.Checkbox('My Checkbox', "RADIO2",key = 'Check2')],

#[sg.Text('Enter something on Row 2'), sg.InputText()],

#sg.Radio('My third radio!', "RADIO1", key='Radio3')],

i = 1
attribute = fields[i]
hits = len(animals)
result = list(animals.keys())
print(attribute)
layout = [
            [sg.Text("Lukas's Dycotomous Quiz")],
            [sg.Text('Is your animal {}?'.format(attribute),key = 'question')],
            [sg.Radio('True', "RADIO1", default=True,key = 'Radio1'),
             sg.Radio('False', "RADIO1",key = 'Radio2')],
            [sg.Button('Next'), sg.Button('Cancel')],
            [sg.Text('I found in my database {} anmials:'.format(hits),key = 'found')],
            [sg.Listbox(result,size=(20,20),background_color='grey',key = 'listbox')],
         ]


# Create the Window
window = sg.Window("Lukas's Dycotomous Quiz", layout)
# Event Loop to process "events" and get the "values" of the inputs

filterstring = ''
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    filterstring += 'a.{}'.format(attribute)
    hits = len([a for a in animals.keys() if filterstring])
    result = [a for a in animals.keys() if filterstring]
    i += 1
    attribute = fields[i]
    #print(attribute)
    print(hits)
    print(filterstring)
    window['question']('Is your animal {}?'.format(attribute))
    window['found']('I found in my database {} anmials:'.format(hits))
    window['listbox'](result)





    #print('You entered ', values[0])
    #print(values['animal'],values['attribute'],'=',animals[values['animal']][values['attribute']])
    #print(values)
window.close()