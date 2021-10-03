N=int(input())
t=[0]*N
x=[0]*N
y=[0]*N
for i in range(N):
    t[i],x[i],y[i]=map(int,input().split())
flag=0
for i in range(N):
    if t[i]%2==0:#偶数
        if (x[i]+y[i])%2==0 and (x[i]+y[i])<=t[i]:
            flag+=0
        else:
            flag+=1
    else:#奇数
        if (x[i]+y[i])%2==1 and (x[i]+y[i])<=t[i]:
            flag+=0
        else:
            flag+=1
for i in range(1,N):
    if abs((x[i]+y[i])-(x[i-1]+y[i-1]) )> t[i]-t[i-1]:
        flag+=1

if flag==0:
    print("Yes")
else:
    print("No")