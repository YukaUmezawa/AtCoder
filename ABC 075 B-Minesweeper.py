H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(list(input()))

for i in range(H):
    for j in range(W):
        c=0
        if S[i][j]==".":
            if i>0:
                if j>0:
                    if S[i-1][j-1]=="#":
                        c+=1
                if S[i-1][j]=="#":
                    c+=1
                if j<W-1:
                    if S[i-1][j+1]=="#":
                        c+=1
            if j>0:
                if S[i][j-1]=="#":
                    c+=1
            if j<W-1:
                if S[i][j+1]=="#":
                    c+=1
            if i<H-1:
                if j>0:
                    if S[i+1][j-1]=="#":
                        c+=1
                if S[i+1][j]=="#":
                    c+=1
                if j<W-1:
                    if S[i+1][j+1]=="#":
                        c+=1
            #del S[i][j]
            S[i][j]=str(c)
            #print(S)
#print(S)
for a in S:
    print(*a,sep="")



