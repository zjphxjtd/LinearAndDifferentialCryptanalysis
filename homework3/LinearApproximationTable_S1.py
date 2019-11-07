import sbox


#int 8位定长2进制
def getbin(x):
    A=[0]*8
    for i in range(8):

        A[7-i]=x%2
        x=int(x/2)
    return A

#按位异或
def XORbit(A,B):#输入为长度为8的0,1数组（二进制表示）
    C=[0]*8
    for i in range(8):
        C[i]=A[i]^B[i]
    return C

#经过SBox得到输出Y
def getY(x):
    i=int(x/16)
    j=x%16
    return sbox.S_1[i][j]

def getIndex(n):
    B = []
    A = getbin(n)
    for i in range(8):
        if A[i] == 1:
            B.append(i)

    return B
LNTable = [ [0] * 256 for i in range(256)]
tag=0
for i in range(256):
    X=getbin(i)
    Y=getbin(getY(i))
    for j in range(256):#每个X的256种位组合
        A=getIndex(j)
        init=0
        #X中选中的元素异或
        for a in A:
            init=init^X[a]
        temp=init
        for k in range(256):#每个Y的256种位组合
            init=temp
            B=getIndex(k)

            #X中选中元素异或结果和Y中选中元素异或
            for b in B:
                init=init^Y[b]
            if init==0:
                LNTable[j][k]+=1

            tag+=1

for i in range(256):
    for j in range(256):
        LNTable[i][j]-=128
LNTable[0][0]=256
print(LNTable)
