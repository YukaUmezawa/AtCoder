N=int(input())
ans=1
d=10**9+7
for i in range(1,N+1):
    ans*=i
    ans=ans%d
print(ans)