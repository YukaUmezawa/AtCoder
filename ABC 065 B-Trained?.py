N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))
c=1
ind=a[0]
flag=False
for i in range(N):
    if ind==2:
        flag=True
        break
    ind=a[ind-1]
    c+=1
if flag==True:
    print(c)
else:
    print(-1)