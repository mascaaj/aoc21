
filename = '..\data\data.txt'
with open(filename) as fn:
    location = [0, 0, 0]
    ln = fn.readline()
    while ln:
        lnsplit = ln.split()
        if lnsplit[0] == 'forward':
            location[0] += int(lnsplit[1])
            location[1] += (location[2]*int(lnsplit[1]))
        else:
            if lnsplit[0] == 'down':
                location[2] += int(lnsplit[1])
            else:
                location[2] -= int(lnsplit[1])
        ln = fn.readline()
    print(location[0]*location[1])
