import sbox

#返回非线性输出
def getdY(dx):
    i=int(dx/16)
    j=dx%16
    return sbox.S_0[i][j]

#初始化差分分析表
dtable=[[[]for i in range(256)]for i in range(256)]
for i in range(256):
    for j in range(256):
        dtable[i][j]=0

#差分分析


t=0
for i in range(256):
    for j in range(256):
        print(t)
        t+=1
        dX=i^j      #输入异或
        Y1=getdY(i)
        Y2=getdY(j)
        dY=Y1^Y2    #输出异或
        dtable[dX][dY]+=1

#打印差分分析表

print(dtable)