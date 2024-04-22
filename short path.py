def short(arr,final,ma,pos):
    if final[0]==pos[0] and final[1]==pos[1]:
        return arr
    import copy as c
    n1,n2,n3,n4=c.deepcopy(arr),c.deepcopy(arr),c.deepcopy(arr),c.deepcopy(arr)
    if (pos[0]-1)>=0:
        if n1[pos[0]-1][pos[1]]==0:
            n1[pos[0]-1][pos[1]]=ma+1
            n1=short(n1,final,ma+1,[pos[0]-1,pos[1]])
        else:
            n1=False
    else:
        n1=False
    if (pos[0]+1)<len(arr):
        if n2[pos[0]+1][pos[1]]==0:
            n2[pos[0]+1][pos[1]]=ma+1
            n2=short(n2,final,ma+1,[pos[0]+1,pos[1]])
        else:
            n2=False
    else:
        n2=False
    if (pos[1]-1)>=0:
        if n3[pos[0]][pos[1]-1]==0:
            n3[pos[0]][pos[1]-1]=ma+1
            n3=short(n3,final,ma+1,[pos[0],pos[1]-1])
        else:
            n3=False
    else:
        n3=False
    if (pos[1]+1)<len(arr):
        if n4[pos[0]][pos[1]+1]==0:
            n4[pos[0]][pos[1]+1]=ma+1
            n4=short(n4,final,ma+1,[pos[0],pos[1]+1])
        else:
            n4=False
    else:
        n4=False
    m1,m2,m3,m4=0,0,0,0
    if n1!=False:
        m1=n1[final[0]][final[1]]
    else:
        m1=len(arr)**2+1
    if n2!=False:
        m2=n2[final[0]][final[1]]
    else:
        m2=len(arr)**2+1
    if n3!=False:
        m3=n3[final[0]][final[1]]
    else:
        m3=len(arr)**2+1
    if n4!=False:
        m4=n4[final[0]][final[1]]
    else:
        m4=len(arr)**2+1
    l1=[n1,n2,n3,n4]
    l=[m1,m2,m3,m4]
    return l1[l.index(min(l))]
r=int(input("Enter no of rows:"))
bx=[[0 for i in range(0,r)]for j in range(0,r)]
while True:
    q=input("Enter yes if u want to add some blockages:")
    if q.upper()=='YES':
        p=tuple(map(int,input("Enter the cordinates with a space:").split()))
        bx[p[0]-1][p[1]-1]=-1
    else:
        break
start=list(map(int,input("Enter the starting cordinates with a space:").split()))
start[0]-=1
start[1]-=1
bx[start[0]][start[1]]=1
end=list(map(int,input("Enter the ending cordinates with a space:").split()))
end[0]-=1
end[1]-=1
op=short(bx,end,1,start)
if op==False:
    print("There is no way to reach the destination")
else:
    for i in range(0,r):
        for j in range(0,r):
            if op[i][j]>0:
                print(op[i][j],end=' ')
            elif op[i][j]==0:
                print("X",end=' ')
            else:
                print("~",end=' ')
        print()
