import re

def arithmetic_arranger(st, *args):
    res = False
    comp=[]
    comp_mx=[]
    err = []
    if len(args) != 0:
        res = args[0]

    for sp in st:
        sepalate = sp.split()
        mx = max(len(sepalate[0]), len(sepalate[1]), len(sepalate[2]))
        if re.search(r'[^0-9]+', sepalate[0]) != None:
            err.append('Error: First Numbers must only contain digits.')
        if re.search(r'[^0-9]+', sepalate[2]) != None:
            err.append('Error: Second Numbers must only contain digits.')
        if (sepalate[1] != '+') & (sepalate[1] != '-'):
            err.append('Error: Operator must be \'+\' or \'-\'.')
        if mx > 4:
            err.append('Error: Numbers cannot be more than four digits.')
        comp.append(sepalate)
        comp_mx.append(mx)

    if len(err) > 6:
        print('Error: Too many problems.')
        exit(len(err))
    if err != []:
        for er in err:
            print(er)
        exit(len(err))


    for line in range(4):
        for i in range(len(comp)):
            if line == 0:
                print(' '*(comp_mx[i]+2-len(comp[i][line])) + comp[i][line], end='')
            elif line == 1:
                print(comp[i][line] + ' '*(comp_mx[i]+1-len(comp[i][line+1])) + comp[i][line+1], end='')
            elif line == 2:
                print('-'*(comp_mx[i]+2), end='')
            elif res == True:
                if comp[i][1] == '+':
                    result = int(comp[i][0]) + int(comp[i][2])
                else:
                    result = int(comp[i][0]) - int(comp[i][2])
                print(' '*(comp_mx[i]+2-len(str(result))) + str(result), end='')
            print(' '*4, end='')
        print('')
