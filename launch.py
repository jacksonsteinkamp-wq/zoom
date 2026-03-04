import subprocess, sys, presetanal, zoom, time
global presetlist
presetlist = []

def clear(): #CHATGPT HELPED ME WITH THIS FUNCTION, I DIDNT KNOW HOW TO CLEAR THE TERMINAL
    print("\033[2J\033[H", end="")
    #print("pretend I cleared here")
    
def firstquestion():
    clear()
    print("What would you like to do?")
    print("0 - Previous Setup")
    print("1 - Presets")
    print("2 - Edit Presets")
    print("3 - Exit")
    return input("Enter the number of your choice: \n") 

def getpresets():
    global presetlist
    presetlist = []
    file = open("presets.txt", "r")
    for line in file:
            presetlist.append(line.strip())
    file.close()
    if presetlist != None:
        return presetlist
    
def select_Which_Preset_Edit_To_Do():
    clear()
    print("Choose an action:")
    print("0 - Create new preset")
    print("1 - Remove a preset")
    print("2 - Edit a preset")
    print("3 - Go Back")
    action = input("Enter the number of your choice: \n")
    if action not in ['0', '1', '2', '3']:
        print("Invalid input, please enter a number from 0 to 3")
        return select_Which_Preset_Edit_To_Do()
    if action == '0': #Add a preset
        clear()
        newpresetname = input("Enter the name of the new preset: \nEnter '0' to go back\n")
        if newpresetname != '0':
            for i in newpresetname:
                if i == ',' or i == '<' or i == '>' or i == '|' or i == '(' or i == ')' or i == ':':
                    print("Presets cannot contain special characters, please try again.")
                    return
            file = open("presets.txt", "a")
            file.write(newpresetname + "\n")
            file.close()
        else:
            print("Going back!") #Just so I remember what this is, too fast to see
            return
    elif action == '1': #Remove a preset
        getpresets()
        if not presetlist:
            print("No presets to remove.")
            return
        print("Choose a preset to remove:\nKey - Preset")
        i = 0
        for preset in presetlist:
            print(str(i) + " - " + preset.split('|')[0])
            i += 1
        try:
            choice = int(input("Enter the number of your choice: \n"))
        except ValueError:
            print("Invalid input — must be a number.")
            return
        if choice < 0 or choice >= len(presetlist):
            print("Choice out of range.")
            return
        presetlist.pop(choice)
        with open("presets.txt", "w") as file:
            for preset in presetlist:
                file.write(preset + "\n")
        return
    elif action == '2':
        Chosen_Preset_To_Edit = choosepreset()
        return Chosen_Preset_To_Edit
    elif action == "3":
        print("Going back!") #Just so I remember what this is, too fast to see
        return 
    
def runpreset(preset):
    print("Not made yet")
    zoom.main(presetanal.readpresetdata(preset))
    
def choosepreset(): #chooses preset to run, then runs it. #TODO implement the running of the preset
    getpresets()
    while True:
        clear()
        print("Choose a preset:")
        i = 0
        for preset in presetlist:
            print(str(i) + " - " + preset.split('|')[0])
            i += 1
        try:
            choice = int(input("Enter the number of your choice: \n"))
        except ValueError:
            print("Invalid input — must be a number. Try again in a second.")
            print('Clearing...')
            time.sleep(1)
            continue
        if choice < 0 or choice >= len(presetlist):
            print("Choice out of range. Try again in a second.")
            print('Clearing...')
            time.sleep(1)
            continue
        if presetlist != None:
            return presetlist[choice]

def previoussetup():
    getpresets()
    for preset in presetlist:
        for char in preset:
            if char == '<':
                strprevioussetupvar = preset 
                print('Found Previous: ' + strprevioussetupvar.split('|')[0] + '\nRunning Previous...' + '\nHold Escape to Quit!')
                return strprevioussetupvar
            else:
                print("No previous setup found, going back to main menu...")
                return None
                
def main():
    while True:
        firstresult = firstquestion()
        if firstresult == '0': #Run preset from the previous time running this file 
            clear()
            print("Running previous setup...")
            setup = previoussetup()
            if setup != None: 
                runpreset(setup)
            else:
                print("No previous setup found. Try something else in a second.")
                print("Clearing...")
                time.sleep(1)
                clear()
                return
                            
        elif firstresult == '1': #Choose a preset from the presets.txt file and run it 
            getpresets()
            preset_to_run = choosepreset()
            if preset_to_run != None:
                clear()
                print("Running preset: " + preset_to_run.split('|')[0] + '\nHold Escape to Quit!')
                runpreset(preset_to_run)
            else:
                return
            
        elif firstresult == '2':
            getpresets()
            Chosen_Preset_To_Edit = select_Which_Preset_Edit_To_Do()
            if Chosen_Preset_To_Edit != None:
                clear()
                print("Editing preset: " + Chosen_Preset_To_Edit.split('|')[0]) 
                presetanal.editpreset(Chosen_Preset_To_Edit)
            #TODO add the editing of preset, and also #TODO somewhere this variable became an integer so this won't work. 
            
        elif firstresult == '3':
            break

        elif firstresult not in ['0', '1', '2', '3']:
            print("Invalid input, please enter a number from 0 to 3")
            continue
        
main() #fuck now everything is running twice. #TODO Ask the big PP
input("Press Enter to close program...") #so the python window doesn't close immediately after running the script, allowing the user to see any output before exiting

''' NOTES

#TODO add the option to choose which monitor (let user know that it is primary be default) IF WE HAVE TIME OFC
#TODO code toggle and AWP (in their own files likely, if we have time)
#TODO if we have time, add option for crosshair offsets (in presets) (won't work across resolutions) (for when a game is not fullscreen, like minecraft or something)
#TODO if we have time, make sure the user can only enter a number when asked for a number, and not a letter or something else that would cause an error. (If we have time ofc)
#TODO make things onkeypress or something so the user doesnt have to hit enter (If we have time ofc)
#TODO if we have time add DPI changer (likely hard ash)
#TODO make it able to be bound to right click
#TODO test on multiple setup
#TODO make sure no duplicate preset names (maybe)
#TODO make sure to understand things

python.analysis.typeCheckingMode <-- I enabled this setting on VSCode

'''