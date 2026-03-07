import time

def clear():
    print("\033[2J\033[H", end="")

def build_entry():
    clear()
    print("0 - Hold")
    print("1 - Toggle")
    print("2 - AWP (Cycle)")
    print("3 - Cancel")
    action = input("Enter the number of your choice: \n")

    if action == '0':
        mode = 'Hold'
    elif action == '1':
        mode = 'Toggle'
    elif action == '2':
        mode = 'AWP'
    elif action == '3':
        return None
    else:
        print("Invalid input.")
        time.sleep(1)
        return build_entry()

    key = input("Enter the key for " + mode + " (e.g. F5, p): \n")

    if mode == 'AWP':
        zooms = input("Enter zoom values separated by commas (e.g. \"2.0, 2.5, 3.0\"): \n")
        return "(" + mode + " : " + key + " : " + zooms + ")"
    else:
        zoom = input("Enter the zoom value (e.g. 4.0): \n")
        return "(" + mode + " : " + key + " : " + zoom + ")"

def get_entries(preset_line):
    entries = []
    i = 0
    while i < len(preset_line):
        if preset_line[i] == '(':
            end = preset_line.index(')', i)
            entries.append(preset_line[i:end+1]) #what the fuck is this even ask once I have wifi again #TODO left
            i = end + 1
        else:
            i += 1
    return entries

def editpreset(preset_line): #TODO fix this (make it work / make user able to go back)
    line = preset_line.replace(' <>', '').strip()
    name = line.split('|')[0].strip()
    entries = get_entries(line)

    while True:
        clear()
        print("Editing: " + name)
        print("Keys:")
        i = 0
        for Name in entries:
            print(str(i) + " - " + Name)
            i += 1
        
        print("\nActions:\n0 - Add a key")
        print("1 - Remove a key")
        print("2 - Rename")
        print("3 - Save and exit")
        print("4 - Cancel")
        choice = input("Enter the number of your choice: \n")

        if choice == '0':
            new_entry = build_entry()
            if new_entry != None:
                entries.append(new_entry)

        elif choice == '1':
            if len(entries) <= 1:
                print("Must have at least one key.")
                time.sleep(1.5)
                continue
            numtoremove = input("Enter the number of the key to remove: \n")
            if int(numtoremove) >= 0 and int(numtoremove) < len(entries):
                entries.pop(int(numtoremove))
            else:
                print("Invalid choice.")
                time.sleep(1)

        elif choice == '2':
            new_name = input("Enter new name (or '0' to cancel): \n")
            if new_name != '0':
                file = open("presets.txt", "r")
                taken = False
                SpecialChar = False
                for line in file:
                    if line.split('|')[0].strip() == new_name.strip():
                        taken = True
                for i in new_name:
                    if i == ',' or i == '<' or i == '>' or i == '|' or i == '(' or i == ')' or i == ':' or i == '\\': #TODO check how this works (the backslash in a string)
                        SpecialChar = True
                if taken:
                    print("A preset with that name already exists, or you did not change the preset name.")
                    time.sleep(2.5)
                elif SpecialChar:
                    print("You cannot use special characters, please try again.")
                    time.sleep(2)                   
                else:
                    name = new_name.strip()

        elif choice == '3': #TODO make sure that there is at least one functional key here and fix in general
            key_count = len(entries)
            save_line = name + " | " + str(key_count) + " " + "".join(entries)
            if ' <>' in preset_line:
                save_line = save_line + ' <>'
            file = open("presets.txt", "r")
            lines = file.readlines()
            file.close()
            file = open("presets.txt", "w")
            for line in lines:
                if line.split('|')[0].strip() == preset_line.split('|')[0].strip():
                    file.write(save_line + "\n")
                else:
                    file.write(line)
            file.close()
            print("Saved!")
            time.sleep(1.5)
            return

        elif choice == '4':
            print("Cancelled.")
            time.sleep(1)
            return
        
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