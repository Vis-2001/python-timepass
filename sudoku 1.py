board=list()
box=list()
for i in range (0,9):
    l=list()
    for j in range(0,9):
        l.append([(i,j),1,2,3,4,5,6,7,8,9])
    box.append(l)

def row(ch):
    for i in range(0,9):
        for j in range(0,9):
            if len(ch[i][j])==2:
                for k in range(0,9):
                    if k!=j:
                        if ch[i][j][1] in ch[i][k]: 
                            ch[i][k].remove(ch[i][j][1])
    for i in range(0,9):
        ele=list()
        for j in range(0,9):
            ele.extend(ch[i][j])
        for j in range(1,10):
            if ele.count(j)==1:
                for k in range(0,9):
                    if j in ch[i][k]:
                        ch[i][k]=(ch[i][k][0],j)
    return ch
def column(ch):
    for i in range(0,9):
        for j in range(0,9):
            if len(ch[j][i])==2:
                for k in range(0,9):
                    if k!=j:
                        if ch[j][i][1] in ch[k][i]: 
                            ch[k][i].remove(ch[j][i][1])
    for i in range(0,9):
        ele=list()
        for j in range(0,9):
            ele.extend(ch[j][i])
        for j in range(1,10):
            if ele.count(j)==1:
                for k in range(0,9):
                    if j in ch[k][i]:
                        ch[k][i]=(ch[k][i][0],j)
    return ch
def square(ch):
    def change(c):
        cng=list()
        for i in range(0,3):
            l1=list(range(i*3,(i+1)*3))
            for j in range(0,3):
                l2=list(range(j*3,(j+1)*3))
                l3=list()
                for k in l1:
                    for l in l2:
                        l3.append((k,l))
                l4=list()
                for k in l3:
                    l4.append(ch[k[0]][k[1]])
                cng.append(l4)
        return cng
    return change(ch)
for i in range(0,9):
    ln=list()
    for j in range(0,9):
        print('enter value of',i+1,'row and',j+1,'cloumn')
        print('enter 0 for no value')
        ln.append(int(input()))
    board.append(ln)
for i in range(0,9):
    for j in range(0,9):
        if board[i][j]!=0:
            box[i][j]=[box[i][j][0],board[i][j]]
res=list()
while res!=box:
    import copy as c
    res=c.deepcopy(box)
    box=square(row(square(column(row(box)))))
for i in range(0,9):
    for j in range(0,9):
        print(box[i][j][1],end=" ")
    print()
