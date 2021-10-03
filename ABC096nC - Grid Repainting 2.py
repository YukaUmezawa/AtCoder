H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(list(input()))
flag=True
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            if i==0:
                if j==0:
                    if S[i][j+1]!="#" and S[i+1][j]!="#":
                        flag=False
                elif j==W-1:
                    if S[i][j-1]!="#" and S[i+1][j]!="#":
                        flag=False
                else:
                    if S[i][j-1]!="#" and S[i+1][j]!="#" and S[i][j+1]!="#":
                        flag=False
            elif i==H-1:
                if j==0:
                    if S[i][j+1]!="#" and S[i-1][j]!="#":
                        flag=False
                elif j==W-1:
                    if S[i][j-1]!="#" and S[i-1][j]!="#":
                        flag=False
                else:
                    if S[i][j-1]!="#" and S[i-1][j]!="#" and S[i][j+1]!="#":
                        flag=False
            else:
                if j==0:
                    if S[i][j+1]!="#" and S[i-1][j]!="#" and S[i+1][j]!="#":
                        flag=False
                elif j==W-1:
                    if S[i][j-1]!="#" and S[i-1][j]!="#" and S[i+1][j]!="#":
                        flag=False
                else:
                    if S[i][j+1]!="#" and S[i][j-1]!="#" and S[i-1][j]!="#" and S[i+1][j]!="#":
                        flag=False

if flag==True:
    print("Yes")
else:
    print("No")