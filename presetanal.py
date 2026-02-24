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

def readpresetdata(preset): #TODO make this work! we are on a good track!
    name = preset.split('|')[0].strip()
    numkeys = preset.split('|')[1].split("(")[0].strip()
    onetype = determine_preset_type(preset)
    if onetype != None:
        print("Key Type: " + str(onetype))
        
        
        
    print("Preset Name: " + name)
    print("Number of Keys: " + numkeys)
    for char in preset:
        if char == '<':
            print('Is previous setup')
            break
    
    
        
def determine_preset_type(preset):#This is the mode, either Toggle, Hold, or AWP. I can use this to determine which function to call in the zoom.py file.  
    if numkeys == 1:    
        return(preset.split('(')[1].split(':')[0].strip())     #TODO make this work with more than one key   
    else:
        return

def update_newestpreset(): #Maybe have this take an argument?
    print("Not made yet") #TODO
