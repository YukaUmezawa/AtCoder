a,b,x=map(int,input().split())
# c=0
# for i in range(a,b+1):
#     if i%x==0:
#         c+=1
# print(c)
dai=b//x
if a==0:
    syou=-1
else:
    syou=(a-1)//x
print(dai-syou)