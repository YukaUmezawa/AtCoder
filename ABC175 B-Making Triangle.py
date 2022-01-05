N=int(input())
L=list(map(int,input().split()))
if N<3:
    print(0)

else:
    c=0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i]==L[j] or L[i]==L[k] or L[k]==L[j]:
                    c+=0
                else:
                    tri=[L[i],L[j],L[k]]
                    maxL=max(tri)
                    other=sum(tri)-maxL
                    if maxL<other:
                        c+=1
    print(c)