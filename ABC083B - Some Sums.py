import math
# L=list(map(int,input().split()))
# N=L[0]
# A=L[1]
# B=L[2]
# # A=string(A)
# # B=string(B)
N=20
A=2
B=5
count=0
for i in range(1,N+1):
    j=i
    if math.floor(i/10000) > 0:
        c10000=math.floor(i/10000)
        i=i-10000*c10000
    else:
        c10000=0
    if math.floor(i/1000) > 0:
        c1000=math.floor(i/1000)
        i=i-1000*c1000
    else:
        c1000=0
    if math.floor(i/100) > 0:
        c100=math.floor(i/100)
        i=i-100*c100
    else:
        c100=0
    if math.floor(i/10) > 0:
        c10=math.floor(i/10)
        i=i-10*c10
    else:
        c10=0
    c_total=c10000+c1000+c100+c10+i
    print(c_total)
    if (c_total>=A) and (c_total<=B):
        count+=j
print(count)