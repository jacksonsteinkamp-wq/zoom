global presetlist
presetlist = []

def firstquestion():
    #TODO find out how to clear terminal and implement ts EVERYWHERE #Just in case the user goes back to this page
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
    #TODO find out how to clear terminal and implement ts EVERYWHERE
    print("Choose a preset:")
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split(',')[0]) #the split is to only show the name of the preset, not the info associated with it  #TODO find out if I can do .strip here
    choice = int(input("Enter the number of your choice: \n"))
    return presetlist[choice]
    
def select_Which_Preset_Edit_To_Do():
    #TODO find out how to clear terminal and implement ts EVERYWHERE
    print("Choose an action:")
    print("0 - Create new preset")
    print("1 - Remove a preset")
    print("2 - Edit a preset")
    print("3 - Go Back")
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
    elif action == "3":
        #TODO find out how to clear terminal and implement ts EVERYWHERE
        print("Going back!")
        firstquestion()
        return #TODO MY DADS A CUCK AND SO I CANT TEST THIS BUT DO SO ASAP

def editpreset(preset):
    exit #TODO implement this
    
def readpresets():
    exit #TODO implement this
    
def writepreset(preset): #May not use this idrk yet
    exit #TODO implement this

def addpreset():
    newpresetname = input("Enter the name of the new preset: \nEnter '0' to go back\n")
    if newpresetname != 0:
        for i in newpresetname:
            if i == ',' or '<' or '>' or '|' or '(' or ')' or ':':
                print("Presets cannot contain special characters, please try again.")
                addpreset()
                return #TODO understand this bullshit (and everything else while we're at it)
        file = open("presets.txt", "a")
        file.write(newpresetname + "\n")
        file.close() #TODO implement the rest
    else:
        #TODO find out how to clear terminal and implement ts EVERYWHERE
        print("Going back!")
        select_Which_Preset_Edit_To_Do()
        return #TODO MY DADS A CUCK AND SO I CANT TEST THIS BUT DO SO ASAP

def removepreset():
    #TODO find out how to clear terminal and implement ts EVERYWHERE
    print("Choose a preset to remove:\nKey - Preset")
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  #TODO find out if I can do .strip here
    choice = int(input("Enter the number of your choice: \n"))
    presetlist.pop(choice)
    file = open("presets.txt", "w")
    for preset in presetlist:
        file.write(preset + "\n")
    file.close()

def selectpreset(): #TODO make this stop at the comma
    #TODO find out how to clear terminal and implement ts EVERYWHERE
    print('Which preset would you like to edit? \nKey - Preset')
    for i, preset in enumerate(presetlist):
        print(str(i) + " - " + preset.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  #TODO find out if I can do .strip here
    choice = presetlist[int(input("Enter the number of your choice: \n"))]
    return choice

def previoussetup():
    getpresets()
    for preset in presetlist:
        #print(preset)
        for char in preset:
            #print(char)
            if char == '<':
                previous = preset 
                print('Found Previous: ' + previous.split('|')[0] + '\nRunning Previous...') #the split is to only show the name of the preset, not the info associated with it
                return previous #TODO MY DADS A CUCK AND SO I CANT TEST THIS BUT DO SO ASAP #TODO learn how to use this shit ass thing

def main():
    firstresult = firstquestion()
    if firstresult == '0': #Just do the preset from the previous time running this file #TODO implement this
        #TODO find out how to clear terminal and implement ts EVERYWHERE
        print("Running previous setup...")
        previoussetup = previoussetup()
        #TODO implement the actual zoom (I have to do this like everywhere tbf)
        
    elif firstresult == '1': #Choose a preset from the presets.txt file and run it #TODO implement this
        getpresets()
        preset_to_run = choosepreset()
        #TODO find out how to clear terminal and implement ts EVERYWHERE
        print("Running preset: " + preset_to_run.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  
        
    elif firstresult == '2': #Edit the presets in the presets.txt file, allowing the user to add, remove, or edit presets #TODO implement this
        getpresets()
        Chosen_Preset_To_Edit = select_Which_Preset_Edit_To_Do()
        if Chosen_Preset_To_Edit != None:
            #TODO find out how to clear terminal and implement ts EVERYWHERE
            print("Editing preset: " + Chosen_Preset_To_Edit.split('|')[0]) #the split is to only show the name of the preset, not the info associated with it  #TODO find out if I can do .strip here
            editpreset(Chosen_Preset_To_Edit)
        firstquestion() #TODO MY DADS A CUCK AND SO I CANT TEST THIS BUT DO SO ASAP
        return
            
    elif firstresult == '3': #Closes program
        exit()

main()
input("Press Enter to close program...") #so the python window doesn't close immediately after running the script, allowing the user to see any output before exiting
#TODO determine where to place the above line. Should it be in line 119?
#TODO determine (once the zoom actually works) if this hit enter bs will actually stop it. I suspect it wont, so better change that somehow. Works for now though

'''
The <> is the previous preset. 
'Name' | 'number of keys' : ("Type of first key" : Keyboard Key : zoom level ) <>
Example 1 | 1 ( Toggle : p : 2.0)
Example 2 | 2 ( Toggle : F5 : 4.0 )( Hold : p : 2.0) <> #This is the most recently used file
Example 3 | 1 (AWP : p : 2.0, 4.0)
Example 4 | 2 (Hold : p : 2.0 )(AWP : F5 : 2.0, 2.5, 3.0, 3.5)
'''