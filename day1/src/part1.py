
filename = '..\data\data.txt'
with open(filename) as fn:
    lncount = 0
    ln = fn.readline()
    while ln:
        lint = int(ln)
        ln = fn.readline()
        if ln:
            if (int(ln)-lint) > 0:
                lncount += 1
                print('increasing')
            else:
                print('decreasing')
    print(lncount)
