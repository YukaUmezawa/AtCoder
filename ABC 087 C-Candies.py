N=int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A=[A1,A2]

#i,j=0
ame_dai=0
for i in range(N):
    ame=sum(A1[:N-i])+sum(A2[-i-1:])
    #print(ame)
    if ame>ame_dai:
        ame_dai=ame
print(ame_dai)
