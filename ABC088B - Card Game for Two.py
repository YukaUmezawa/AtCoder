N=int(input())
L=list(map(int,input().split()))
L.sort(reverse=True)
A=0
B=0
for x in range(len(L)):
    if x%2==0:
        A+=L[x]
    else:
        B+=L[x]
print(A-B)