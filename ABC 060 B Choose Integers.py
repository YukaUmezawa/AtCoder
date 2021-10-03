A,B,C=map(int,input().split())
#amari=A%B
#num=1
flag=False
# if amari!=C:
for i in range(1,B+1):
    num=A*i
    amari=num%B
    if amari==C:
        print("YES")
        flag=True
        break
if flag==False:
    print("NO")
