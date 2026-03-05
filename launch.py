import subprocess, sys, presetanal, zoom, time, preseteditor
global presetlist
presetlist = []

zoom.imports()

def clear(): #CHATGPT HELPED ME WITH THIS FUNCTION, I DIDNT KNOW HOW TO CLEAR THE TERMINAL
    print("\033[2J\033[H", end="")
    
def firstquestion():
    clear()
    print("What would you like to do?")
    print("0 - Previous Setup")
    print("1 - Presets")
    print("2 - Edit Presets")
    print("3 - Exit")
    return input("Enter the number of your choice: \n") 

def updaterecent(presetname):
    file = open("presets.txt", "r")
    lines = file.readlines()
    file.close()
    writelines = []
    for line in lines:
        name = line.split('|')[0].strip()
        line = line.replace(' <>','')
        if name == presetname.strip():
            line = line.replace('\n', ' <>\n')
        writelines.append(line)
    file = open("presets.txt", "w")
    for line in writelines:
        file.write(line)
    file.close()
            
def getpresets():
    global presetlist
    presetlist = []
    file = open("presets.txt", "r")
    for line in file:
            presetlist.append(line.strip())
    file.close()

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
    
    if action == '0':
        clear()
        newpresetname = input("Enter the name of the new preset: \nEnter '0' to go back\n")
        if newpresetname != '0':
            getpresets()
            for preset in presetlist:
                if newpresetname == preset.split('|')[0].strip():
                    print("Presets cannot be repeats, please try again.")
                    time.sleep(1.5)
                    return
            for i in newpresetname:
                if i == ',' or i == '<' or i == '>' or i == '|' or i == '(' or i == ')' or i == ':':
                    print("Presets cannot contain special characters, please try again.")
                    time.sleep(1.5)
                    return
            file = open("presets.txt", "a")
            file.write(newpresetname + "\n")
            file.close()
        else:
            print("Going back!")
            time.sleep(1.5)
            return
        
    elif action == '1':
        getpresets()
        if not presetlist:
            print("No presets to remove.")
            time.sleep(1.5)
            return
        print("Choose a preset to remove:\nKey - Preset")
        i = 0
        for preset in presetlist:
            print(str(i) + " - " + preset.split('|')[0])
            i += 1
        choice = input("Enter the number of your choice: \n")
        if type(choice) is not int:
            print("Invalid input — must be a number. Try again in a second.")
            print('Clearing...')
            time.sleep(1.5)
            return
        if choice < 0 or choice >= len(presetlist):
            print("Choice out of range.")
            time.sleep(1.5)
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
        print("Going back!")
        time.sleep(1.5)
        return 
    
def choosepreset():
    getpresets()
    while True:
        clear()
        print("Choose a preset:")
        i = 0
        for preset in presetlist:
            print(str(i) + " - " + preset.split('|')[0])
            i += 1
        choice = int(input("Enter the number of your choice: \n"))
        if type(choice) is not int:
            print("Invalid input — must be a number. Try again in a second.")
            print('Clearing...')
            time.sleep(1)
            continue
        if choice < 0 or choice >= len(presetlist):
            print("Choice out of range. Try again in a second.")
            print('Clearing...')
            time.sleep(1)
            continue
        return presetlist[choice]

def main():
    while True:
        firstresult = firstquestion()
        if firstresult == '0':
            found = False
            clear()
            print("Running previous setup...")
            getpresets()
            for preset in presetlist:
                for char in preset:
                    if char == '<':
                        previous = preset 
                        print('Found Previous: ' + previous.split('|')[0] + '\nRunning Previous...' + '\nHold Escape to Quit!')
                        time.sleep(2)
                        zoom.main(presetanal.readpresetdata(previous))
                        found = True
                        break
                if found:
                    break
            if not found:    
                print("No previous setup found, going back to main menu...")
                time.sleep(1.5)
            clear()
            continue                   
                            
        elif firstresult == '1':
            getpresets()
            preset_to_run = choosepreset()
            if preset_to_run != None:
                clear()
                print("Running preset: " + preset_to_run.split('|')[0] + '\nStarting! Hold Escape to Close.')
                time.sleep(2)
                updaterecent(preset_to_run.split('|')[0].strip())
                zoom.main(presetanal.readpresetdata(preset_to_run))
            else:
                continue
            
        elif firstresult == '2':
            getpresets()
            Chosen_Preset_To_Edit = select_Which_Preset_Edit_To_Do()
            if Chosen_Preset_To_Edit != None:
                clear()
                print("Editing preset: " + Chosen_Preset_To_Edit.split('|')[0])
                time.sleep(2)
                preseteditor.editpreset(Chosen_Preset_To_Edit)
            else:
                continue
            #TODO add the editing of preset (editing and creating)
            
        elif firstresult == '3':
            exit()

        elif firstresult not in ['0', '1', '2', '3']:
            print("Invalid input, please enter a number from 0 to 3")
            time.sleep(2)
            continue

main()
input("Press Enter to close program...")

''' NOTES

#TODO add the option to choose which monitor (let user know that it is primary be default) IF WE HAVE TIME OFC, maybe not for CSP but for myself
#TODO code toggle and AWP (if we have time)
#TODO if we have time, make sure the user can only enter a number when asked for a number, and not a letter or something else that would cause an error. (If we have time ofc, maybe not for CSP but for myself)
#TODO make things onkeypress or something so the user doesnt have to hit enter (If we have time ofc maybe not for CSP but for myself)
#TODO make github (mention dpi button) not for csp though
#TODO make it able to be bound to right click maybe not for CSP but for myself
#TODO test on multiple setup
#TODO make sure no duplicate preset names (maybe)
#TODO make sure to understand things FOR CSP

if mouse.is_pressed("right"):
Valid names: (maybe mention this (and valid key names) in the readme / pdf)
"left"
"right"
"middle"
"x"
"x2"

'''