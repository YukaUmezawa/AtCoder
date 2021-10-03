N,Y=map(int,input().split())
flag=False
success=False
for x in range(N+1):
    mai10000=10000*x
    for y in range(N+1-x):
        mai5000=5000*y
        z=N-x-y
        mai1000=1000*z
        total=mai10000+mai5000+mai1000
        if total==Y:
            print(x,y,z)
            success=True
            flag=True
            break
    if flag==True:
      break
if success!=True:
  print(-1,-1,-1)