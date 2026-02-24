string = 'Example 4 | 2 (Hold : p : 2.0 )(AWP : F5 : 2.0, 2.5, 3.0, 3.5)'
charlist = list(string.split('|')[1])
charlist.pop(0)
charlist.pop(0)
string2 = ''.join(charlist)
keyslist = string2.split('(') #We could I guess determine the amount of keys in the preset by the amount of ( in the string, but this is fine ig (#TODO decide whether to come back and fix)
keyslist.pop(0)
print(keyslist)
for i in range(len(keyslist)):
    keyslist[i] = keyslist[i].replace(')', '')
print(keyslist)