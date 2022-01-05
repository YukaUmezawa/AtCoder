K,S=map(int,input().split())
toatal=0
c=0
for x in range(K+1):
    for y in range(K+1):
        remain=S-(x+y)
        if remain <= K and remain>=0:
            c+=1
print(c)