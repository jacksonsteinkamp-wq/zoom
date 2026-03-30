import time

def clear(): #CHATGPT told me that this fakes clearing the terminal and it does, just not the built in vscode one
    print("\033[2J\033[H", end="")

#Claude code (entire rest of the file with a teensy bit of help from me)
def build_entry(entries):
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
        return build_entry(entries)
    while True:
        key = input("Enter the key for " + mode + " (e.g. F5, p): \n")
        duplicate = False
        for entry in entries:
            if entry.split(':')[1].strip() == key.strip():
                duplicate = True
                break
        if duplicate:
            print("That key is already used in this preset, try again.")
            time.sleep(1.5)
            clear()
        else:
            break
    if mode == 'AWP':
        while True:
            zooms = input('Enter zoom values separated by commas (e.g. "2.0, 2.5, 3.0"): \n')
            zoomlist = zooms.split(",")
            valid = True
            for i in zoomlist:
                if float(i.strip()) <= 1:
                    print("All values must be above 1, try again.")
                    time.sleep(1.5)
                    clear()
                    valid = False
                    break
            if valid:
                break
        return "(" + mode + " : " + key + " : " + zooms + ")"
    else:
        while True:
            zoom = input("Enter the zoom value (e.g. 4.0): \n")
            if float(zoom) <= 1:
                print("Must be above 1, try again.")
                time.sleep(1.5)
                clear()
                continue
            break
        return "(" + mode + " : " + key + " : " + zoom + ")" 

def get_entries(preset_line):
    entries = []
    if '(' not in preset_line:
        return entries
    i = 0
    while i < len(preset_line):
        if preset_line[i] == '(':
            end = preset_line.index(')', i)
            entries.append(preset_line[i:end+1])
            i = end + 1
        else:
            i += 1
    return entries

def editpreset(preset_line):
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
        
        print("Actions:\n0 - Add a key")
        print("1 - Remove a key")
        print("2 - Rename")
        print("3 - Save and exit")
        print("4 - Cancel")
        choice = input("Enter the mode of your choice: \n")

        if choice == '0':
            new_entry = build_entry(entries)
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
                    if i == ',' or i == '<' or i == '>' or i == '|' or i == '(' or i == ')' or i == ':' or i == '\\':
                        SpecialChar = True
                if taken:
                    print("A preset with that name already exists, or you did not change the preset name.")
                    time.sleep(2.5)
                elif SpecialChar:
                    print("You cannot use special characters, please try again.")
                    time.sleep(2)                   
                else:
                    name = new_name.strip()

        elif choice == '3':
            if len(entries) == 0:
                print("Cannot save with no keys. Add at least one key first.")
                time.sleep(1.5)
                continue
            key_count = len(entries)
            save_line = name + " | " + str(key_count) + " " + "".join(entries)
            if ' <>' in preset_line:
                save_line = save_line + ' <>\n'
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
            clear()
            return

        elif choice == '4':
            print("Cancelled.")
            time.sleep(1)
            return
        else: 
            print("Invalid Choice. Please try again")
            time.sleep(1.5)
#Claude ends   