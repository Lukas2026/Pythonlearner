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
result2 = list(animals.keys())

#print(attribute)
attributes_true = []
attributes_false = []
layout = [
            [sg.Text("Lukas's Dycotomous Quiz")],
            [sg.Text("True Filters:", size=(11,1)), sg.Text("False Filters:", size=(10,1))],
            [
                sg.Listbox(attributes_true,  size=(10,10),background_color='grey', key="attr1"),
                sg.Listbox(attributes_false, size=(10,10),background_color='grey', key="attr2"),
             ],
            [sg.Text('Is your animal a {}?'.format(attribute),key = 'question', size=(30,1))],
            [sg.Radio('True', "RADIO1", key = 'Radio1', visible=True, enable_events=True),
             sg.Radio('False', "RADIO1",key = 'Radio2', visible=True, enable_events=True)],
            [sg.Button('Next'), sg.Button('Cancel')],
            [sg.Text('I found in my database {} anmials:'.format(hits),key = 'found')],
            [sg.Listbox(result,size=(20,20),background_color='grey',key = 'listbox')],
         ]



# Create the Window
window = sg.Window("Lukas's Dycotomous Quiz", layout)
# Event Loop to process "events" and get the "values" of the inputs

filterstring = []
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event == "Radio1":
        #print("Radio1 geklickt")
        result = [a for a in result2 if animals[a][attribute]]

    if event == "Radio2":
        #print("Radio2 geklickt")
        result = [a for a in result2 if not animals[a][attribute]]

    if event == "Next":
        if not values["Radio1"] and not values["Radio2"]:
            #print("bitte zuerst Radiobuttons klicken")
            sg.Popup("bitte zuerst True oder False auswählen")
            continue
        if values["Radio1"]:
            attributes_true.append(attribute)
        else:
            attributes_false.append(attribute)
        window["attr1"](attributes_true)
        window["attr2"](attributes_false)
        result = []
        for a in animals.keys():
            ok = True
            for t in attributes_true:
                if not animals[a][t]:
                    ok = False
                    break
            #if ok:
            for t in attributes_false:
                if animals[a][t]:
                    ok = False
                    break
            if ok:
                result.append(a)
        # backup result
        result2 = [a for a in result]
        # reset radios
        window.Element('Radio1').TKIntVar.set(0) # clear both Radio buttons
        #values["Radio1"] = False
        #window["Radio1"](None)
        #window["Radio1"](False)
        
        # prepare next question
        i += 1
        attribute = fields[i]
        window['question']('Is your animal {}?'.format(attribute))
        window.read()

    # ---- always ----
    hits = len(result)
    window['found']('I found in my database {} anmials:'.format(hits))
    window['listbox'](result)
    if hits == 1:
        print("hurra")
    
    #window.read()
        

window.close()
