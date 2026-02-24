#TODO rename this document (here and in launch.py)


def editpreset(preset):
    exit #TODO
    
    
    
def importpresetlist():
    global presetlist
    import launch
    presetlist = launch.getpresets()
    return presetlist

def readpresetdata():
    for preset in importpresetlist():
        name = preset.split('|')[0].strip()
        numkeys = preset.split('|')[1].split("(")[0].strip()
        print(determine_preset_type(preset))
        print("Preset Name: " + name)
        print("Number of Keys: " + numkeys)
    
    
def determine_preset_type(preset):
        return(preset.split('(')[1].split(':')[0].strip()) #This is the mode, either Toggle, Hold, or AWP. I can use this to determine which function to call in the zoom.py file.  
        

def update_newestpreset(): #Maybe have this take an argument?
    exit #TODO
    
    
def getpresets():
    #presetlist.clear()

    try:
        with open("presets.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                recent = "<>" in line
                line = line.replace("<>", "").strip()

                name_part, rest = line.split("|", 1)
                name = name_part.strip()

                preset = {
                    "name": name,
                    "keys": [],
                    "recent": recent
                }

                # find all (...) groups
                parts = rest.split("(")

                for part in parts[1:]:
                    keydata = part.split(")")[0]

                    mode, key, zooms = keydata.split(":")

                    zoom_levels = [
                        float(z.strip())
                        for z in zooms.split(",")
                    ]

                    preset["keys"].append({
                        "mode": mode.strip(),
                        "key": key.strip(),
                        "zoom_levels": zoom_levels
                    })

                #presetlist.append(preset)

    except FileNotFoundError:
        open("presets.txt", "w").close()