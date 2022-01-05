from itertools import product

N,M,X=map(int,input().split())
C = [0]*N
A=[]
for i in range(N):
    l = list(map(int, input().split()))
    C[i]=l[0]
    A.append(l[1:])

# #A[[2, 2, 4], [8, 7, 9], [2, 3, 9]]
flag=False
before_price=float('inf')
for bits_list in product((0,1),repeat=N):#(0,1,0)
    price=0
    understood=[0]*M
    for index,bit in enumerate(bits_list):
        if bit==1:
            price+=C[index]
            for i in range(M):
                understood[i]+=A[index][i]
    ##理解度確認
    count=0
    for i in range(M):
        if understood[i]>=X:
            count+=1
        else:
            break
    if count==M:
        flag=True
        before_price=min(price, before_price)
if flag==False:
    print(-1)
else:
    print(before_price)



