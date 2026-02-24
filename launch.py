import subprocess, sys, presetanal, zoom
global presetlist
presetlist = []

def clear(): #CHATGPT HELPED ME WITH THIS FUNCTION, I DIDNT KNOW HOW TO CLEAR THE TERMINAL
    #print("\033[2J\033[H", end="")
    print("Cleared terminal!") #Just for testing, to make sure it works. Will remove later. (WORKED)
    
def firstquestion():
    clear()
    print("What would you like to do?")
    print("0 - Previous Setup")
    print("1 - Presets")
    print("2 - Edit Presets")
    print("3 - Exit")
    return input("Enter the number of your choice: \n") #TODO make it onkeypress or something so the user doesnt have to hit enter (If we have time ofc)

def getpresets():
    presetlist.clear()
    file = open("presets.txt", "r")
    for line in file:
        presetlist.append(line.strip())
    file.close()
    return presetlist
    
def choosepreset(): #chooses preset to run, then runs it. #TODO implement the running of the preset
    clear()
    print("Choose a preset:")
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split('|')[0]) #TODO find out if I can/should do .strip here
    choice = int(input("Enter the number of your choice: \n"))
    if type(choice) != int:
        print("Invalid input, please use a number.")
        return choosepreset()
    return presetlist[choice]
    
def select_Which_Preset_Edit_To_Do():
    clear()
    print("Choose an action:")
    print("0 - Create new preset")
    print("1 - Remove a preset")
    print("2 - Edit a preset")
    print("3 - Go Back")
    action = input("Enter the number of your choice: \n") #TODO if we have time, make it onkeypress or something so the user doesnt have to hit enter (If we have time ofc)
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
        print("Choose a preset to remove:\nKey - Preset")
        for i, preset in enumerate(presetlist):
            print(str(i) + " - " + preset.split('|')[0])  #TODO find out if I can do .strip here
        choice = int(input("Enter the number of your choice: \n"))
        presetlist.pop(choice)
        file = open("presets.txt", "w")
        for preset in presetlist:
            file.write(preset + "\n")
        file.close()
        return None
    elif action == '2':
        Chosen_Preset_To_Edit = selectpreset()
        return Chosen_Preset_To_Edit
    elif action == "3":
        print("Going back!") #Just so I remember what this is, too fast to see
        return 


    
def runpreset(preset):
    exit #TODO implement this (MAYBE)(HARD). Will definitely use other py file(s) for this. Include 'if None"
    
def selectpreset():
    getpresets()
    clear()
    print('Which preset would you like to edit? \nKey - Preset')
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split('|')[0])  #TODO find out if I can do .strip here
    choice = presetlist[int(input("Enter the number of your choice: \n"))]
    return choice

def previoussetup():
    getpresets()
    for preset in presetlist:
        for char in preset:
            if char == '<':
                strprevioussetupvar = preset 
                print('Found Previous: ' + strprevioussetupvar.split('|')[0] + '\nRunning Previous...')
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
            runpreset(previoussetup())
            
        elif firstresult == '1': #Choose a preset from the presets.txt file and run it 
            getpresets()
            preset_to_run = choosepreset()
            clear()
            print("Running preset: " + preset_to_run.split('|')[0])
            runpreset(preset_to_run)
            
        elif firstresult == '2': #Edit the presets in the presets.txt file, allowing the user to add, remove, or edit presets 
            getpresets()
            Chosen_Preset_To_Edit = select_Which_Preset_Edit_To_Do()
            if Chosen_Preset_To_Edit != None:
                clear()
                print("Editing preset: " + Chosen_Preset_To_Edit.split('|')[0])  #TODO find out if I can/should do .strip here
                presetanal.editpreset(Chosen_Preset_To_Edit)
            
        elif firstresult == '3':
            break

        elif firstresult == "openzoom":
            zoom.main() #This is just for testing, to make sure I can run the zoom script from this file. Will remove later. (WORKED)
            
        elif firstresult == "readdata": #TODO ask PP for some reason this one makes me enter 'e' twice idk why (just for testing though so idk if it matters, I can also just put it above the main())
            presetanal.readpresetdatav2() #This is just for testing, to make sure I can run the presetanal script from this file. Will remove later. (WORKED)
        
        elif firstresult == "findpresettype":
            getpresets()
            presetanal.determine_preset_type(selectpreset()) #This is just for testing, to make sure I can run the presetanal script from this file. Will remove later. (WORKED)

        elif firstresult not in ['0', '1', '2', '3']:
            print("Invalid input, please enter a number from 0 to 3")
            continue
presetanal.isolatekeys(selectpreset()) #This one also makes me enter twice, so I suspect that the issue is in the select presets function
main()
input("Press Enter to close program...") #so the python window doesn't close immediately after running the script, allowing the user to see any output before exiting
#TODO make it so when the user exits, it maybe closes the window / turns off zoom script. If we have time ofc. Also, again if we have time, make any key do this, not just enter.

''' NOTES

The <> is the marker of the previous preset. 
'Name' | 'number of keys' : ("Type of first key" : Keyboard Key : zoom level ) <>
Example 1 | 1 ( Toggle : p : 2.0)
Example 2 | 2 ( Toggle : F5 : 4.0 )( Hold : p : 2.0) <> #This is the most recently used file
Example 3 | 1 (AWP : p : 2.0, 4.0)
Example 4 | 2 (Hold : p : 2.0 )(AWP : F5 : 2.0, 2.5, 3.0, 3.5)

subprocess.run([sys.executable, "zoom.py"]) #used chatgpt #USE THIS
'''

#TODO remove some functions (example remove preset), more files, library/definition?
#TODO if we have time, make sure the user can only enter a number when asked for a number, and not a letter or something else that would cause an error. (If we have time ofc)