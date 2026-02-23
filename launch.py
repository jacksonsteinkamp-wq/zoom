import sys, subprocess, ctypes, time 
global presetlist
presetlist = []

def firstquestion():
    print("What would you like to do?")
    print("0 - Previous Setup")
    print("1 - Presets")
    print("2 - Edit Presets")
    print("3 - Exit")
    return input("Enter the number of your choice: \n") #TODO make it onkeypress or something so the user doesnt have to hit enter (If we have time ofc)

def getpresets():
    file = open("presets.txt", "r")
    for line in file:
        presetlist.append(line.strip()) #the strip is to remove the newline character at the end of each line  
    file.close()
    
def choosepreset(): #chooses preset to run, then runs it. #TODO implement the running of the preset
    print("Choose a preset:")
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split(',')[0]) #the split is to only show the name of the preset, not the info associated with it  
    choice = int(input("Enter the number of your choice: \n"))
    return presetlist[choice]
    
def select_Which_Preset_Edit_To_Do():
    print("Choose an action:")
    print("0 - Create new preset")
    print("1 - Remove a preset")
    print("2 - Edit a preset")
    action = input("Enter the number of your choice: \n")
    if action == '0':
        addpreset()
        return None
    elif action == '1':
        removepreset()
        return None
    elif action == '2':
        Chosen_Preset_To_Edit = selectpreset()
        return Chosen_Preset_To_Edit

def editpreset(preset):
    exit #TODO implement this

def addpreset():
    preset = input("Enter the name of the new preset: \n")
    for i in preset:
        if i == ',':
            print("Presets cannot contain commas, please try again.")
            addpreset()
            return #TODO understand this bullshit
    file = open("presets.txt", "a")
    file.write(preset + "\n")
    file.close() #TODO implement the rest

def removepreset():
    print("Choose a preset to remove:\nKey - Preset")
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  
    choice = int(input("Enter the number of your choice: \n"))
    presetlist.pop(choice)
    file = open("presets.txt", "w")
    for preset in presetlist:
        file.write(preset + "\n")
    file.close()

def selectpreset(): #TODO make this stop at the comma
    print('Which preset would you like to edit? \nKey - Preset')
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  
    choice = presetlist[int(input("Enter the number of your choice: \n"))]
    return choice

def previoussetup():
    exit #TODO implement this

firstresult = firstquestion()
if firstresult == '0': #Just do the preset from the previous time running this file #TODO implement this
    print("Running previous setup...")
    previoussetup()
elif firstresult == '1': #Choose a preset from the presets.txt file and run it #TODO implement this
    getpresets()
    preset_to_run = choosepreset()
    print("Running preset: " + preset_to_run.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  
elif firstresult == '2': #Edit the presets in the presets.txt file, allowing the user to add, remove, or edit presets #TODO implement this
    getpresets()
    Chosen_Preset_To_Edit = select_Which_Preset_Edit_To_Do()
    if Chosen_Preset_To_Edit != None:
        print("Editing preset: " + Chosen_Preset_To_Edit.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  
        editpreset(Chosen_Preset_To_Edit)
        
elif firstresult == '3': #Closes program
    exit()

input("Press Enter to exit...") #so the python window doesn't close immediately after running the script, allowing the user to see any output before exiting


'''
IDEAS FOR SHIT ASS .txt PRESET SETUP
'Name' | 'number of keys' : ("Type of first key" : Keyboard Key : zoom level ) 
Example | 1 ( Toggle : p : 2.0)
Example 2 | 2 ( Toggle : F5 : 4.0 )( Hold : p : 2.0)
Example 3 | 1 (AWP : p : 2.0, 4.0)
Example 4 | 2 (Hold : p : 2.0 )(AWP : F5 : 2.0, 2.5, 3.0)
'''