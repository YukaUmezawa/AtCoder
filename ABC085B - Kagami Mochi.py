N=int(input())
d=[]
c=[]
count=0
maxx=101
for _ in range(N):
    d.append(int(input()))

for i in range(maxx):
    c.append(None)

for i in range(len(d)):
    c[d[i]]=d[i]

for x in range(maxx):
    if c[x]!=None:
        count+=1
print(count)