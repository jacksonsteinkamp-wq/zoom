def isolatekeys(chosenpreset):
    charlist = list(chosenpreset.split('|')[1])
    charlist.pop(0)
    charlist.pop(0)
    string2 = ''.join(charlist)
    keyslist = string2.split('(')
    keyslist.pop(0)
    for i in range(len(keyslist)):
        keyslist[i] = keyslist[i].replace(')', '').replace('<', '').replace('>', '')
    return(keyslist)
    
def importpresetlist():
    global presetlist
    presetlist = []
    presetlist = launch.getpresets() # type: ignore
    return

def readpresetdata(preset):
    preset = preset.strip()
    name = preset.split('|')[0].strip()
    numkeys = preset.split('|')[1].split("(")[0].strip()
    #TODO could I just do this? I don't ever use this is previous thing (I did it, make sure ts works)
    for x in range(len(preset)):
        preset = preset.replace('<>','')
    keys = []
    keyno = 1
    keysraw = isolatekeys(preset)
    for keydata in keysraw:
        mode, key, zooms = keydata.split(":")
        zoomlevels = []
        for times in zooms.split(','):
            zoomlevels.append(float(times.strip()))
        keys.append((mode.strip(), key.strip(), zoomlevels))
        keyno += 1
    return[name, int(numkeys), keys]

def clear():
    launch.clear() # type: ignore
    
def choosepreset():
    launch.getpresets() # type: ignore
    while True:
        clear()
        print("Choose a preset:")
        i = 0
        print('99 - Go Back')
        for preset in presetlist:
            print(str(i) + " - " + preset.split('|')[0])
            i += 1
        choice = int(input("Enter the number of your choice: \n"))
        if type(choice) is not int:
            print("Invalid input — must be a number. Try again in a second.")
            time.sleep(1) # type: ignore
            continue
        if choice == 99:
            print("Going Back...")
            time.sleep(1) # type: ignore
            return 99
        elif choice < 0 or choice >= len(presetlist):
            print("Choice out of range. Try again in a second.")
            time.sleep(1) # type: ignore
            continue
        return presetlist[choice]