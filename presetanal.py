def editpreset(preset):
    print("Not made yet") #TODO
    
def isolatekeys(chosenpreset):
    importpresetlist()
    charlist = list(chosenpreset.split('|')[1])
    charlist.pop(0)
    charlist.pop(0)
    string2 = ''.join(charlist)
    keyslist = string2.split('(') #We could I guess determine the amount of keys in the preset by the amount of ( in the string, but this is fine ig (#TODO decide whether to come back and fix)
    keyslist.pop(0)
    for i in range(len(keyslist)):
        keyslist[i] = keyslist[i].replace(')', '').replace('<', '').replace('>', '')
    print(keyslist) #temp
    
def importpresetlist():
    global presetlist
    import launch
    presetlist = []
    presetlist = launch.getpresets()
    return

def readpresetdata(preset): #TODO make this work! we are on a good track!
    name = preset.split('|')[0].strip()
    numkeys = preset.split('|')[1].split("(")[0].strip()
    if numkeys == '1':
        onetype = determine_preset_type(preset)
        print("Key Type: " + str(onetype))
    else:
        exit ()#TODO (something to do with determine_preset_types_plural()
        
    print("Preset Name: " + name)
    print("Number of Keys: " + numkeys)
    for char in preset:
        if char == '<':
            print('Is previous setup')
            break   
        
def determine_preset_types_plural():
    exit() #TODO
        
def determine_preset_type(preset):#This is the mode, either Toggle, Hold, or AWP. I can use this to determine which function to call in the zoom.py file. This is for one key
    if int(preset.split('|')[1].split("(")[0].strip()) == 1:    
        return(str(preset.split('(')[1].split(':')[0].strip()))

def update_newestpreset(): #Maybe have this take an argument?
    print("Not made yet") #TODO
