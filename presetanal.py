#TODO rename this document (here and in launch.py)

def editpreset(preset):
    exit #TODO
    
    
    
def importpresetlist():
    global presetlist
    import launch
    presetlist = launch.getpresets()

def readpresetdata(): #Just for testing for now
    importpresetlist()
    for preset in (presetlist):
        name = preset.split('|')[0].strip()
        numkeys = preset.split('|')[1].split("(")[0].strip()
        zooms = preset.split(')')[0].split(':')[2].strip().split(",")
        print("Preset Name: " + name)
        print("Number of Keys: " + numkeys)
        for char in preset:
            if char == '<':
                print('Is previous setup')
                break
        if numkeys == '1':
            print(determine_preset_type(preset)) #TODO make this work for things with multiple keys (currently only works for 1 key, which is what I have for testing so it works for now but will need to be fixed eventually)
        else:
            print("Multiple keys, not currently supported for testing so skipping preset type")
        print("Zoom Level(s): " + str(zooms) + " currently only works if theres only one key, which is what I have for testing so it works for now but will need to be fixed eventually") 
        
def readpresetdatav2():
    importpresetlist()
    for preset in (presetlist):
        numkeys = int(preset.split('|')[1].split("(")[0].strip())
        keydatalist = preset.split('(')
        
        
        
        

        
def determine_preset_type(preset):
        return(preset.split('(')[1].split(':')[0].strip()) #This is the mode, either Toggle, Hold, or AWP. I can use this to determine which function to call in the zoom.py file.  
        
def update_newestpreset(): #Maybe have this take an argument?
    exit #TODO
