#TODO rename this document (here and in launch.py)

def editpreset(preset):
    exit #TODO
    
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

def readpresetdata(preset): #Just for testing for now
    name = preset.split('|')[0].strip()
    numkeys = preset.split('|')[1].split("(")[0].strip()
    print("Preset Name: " + name)
    print("Number of Keys: " + numkeys)
    for char in preset:
        if char == '<':
            print('Is previous setup')
            break
    '''if numkeys == '1':
        print(determine_preset_type(preset)) #TODO make this work for things with multiple keys (currently only works for 1 key, which is what I have for testing so it works for now but will need to be fixed eventually)
    else:
        print("Multiple keys, not currently supported for testing so skipping preset type")
    ''' #TODO make this work! we are on a good track!
        
def determine_preset_type(preset):
        return(preset.split('(')[1].split(':')[0].strip()) #This is the mode, either Toggle, Hold, or AWP. I can use this to determine which function to call in the zoom.py file.  
        
def update_newestpreset(): #Maybe have this take an argument?
    exit #TODO
