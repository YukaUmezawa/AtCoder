# from itertools import product

# N=int(input())

# A=[]
# X=[]#[[2,3],[3,1],[1,2]]
# Y=[]#[[1,0],[1,0],[1,0]]

# for i in range(N):
#     a=int(input())
#     if a==0:
#         X.append([])
#         Y.append([])
#     else:
#         A.append(a)
#         xy = [map(int, input().split()) for _ in range(a)]
#         x, y = [list(i) for i in zip(*xy)]
#         X.append(x)
#         Y.append(y)




# for bits_list in product((1,0),repeat=N):
#     for index, T_F in enumerate(bits_list):#(0,1,0)
#         flag=True
#         # print(bits_list)
#         for person in range(N):
#             for i in range(len(X[person])):#[[2,3],[3,1],[1,2]]のはじめの[2,3]
#                 if bits_list[person]==1:#本当
#                     if Y[person][i]==1 and bits_list[X[person][i]-1]==1:
#                         pass
#                         # print("OK1",Y[person][i],person,flag)
#                     elif Y[person][i]==0 and bits_list[X[person][i]-1]==0:
#                         pass
#                         # print("OK1",Y[person][i],person,flag)
#                     else:
#                         flag=False
#                         # print("NG",Y[person][i],person,flag)
#                         break
#                 else:#嘘人
#                     if Y[person][i]==1 and bits_list[X[person][i]-1]==0:
#                         pass
#                         # print("OK1",Y[person][i],person,flag)
#                     elif Y[person][i]==0 and bits_list[X[person][i]-1]==1:
#                         pass
#                         # print("OK1",Y[person][i],person,flag)
#                     else:
#                         flag=False
#                         # print("NG",Y[person][i],person,flag)
#                         break
#             if flag==False:
#                 break
#         if flag==False:
#                 break
#         flag=True
#         print(sum(x==1 for x in bits_list))
#         break
#     if flag==True:
#         break
# if flag==False:
#     print(0)

from itertools import product

N=int(input())

A=[]
X=[]#[[2,3],[3,1],[1,2]]
Y=[]#[[1,0],[1,0],[1,0]]

for i in range(N):
    a=int(input())
    if a==0:
        X.append([])
        Y.append([])
    else:
        A.append(a)
        xy = [map(int, input().split()) for _ in range(a)]
        x, y = [list(i) for i in zip(*xy)]
        X.append(x)
        Y.append(y)



bef=0
for bits_list in product((1,0),repeat=N):
    for index, T_F in enumerate(bits_list):#(0,1,0)
        flag=True
        # print(bits_list)
        for person in range(N):
            if len(X[person])>0:
                for i in range(len(X[person])):#[[2,3],[3,1],[1,2]]のはじめの[2,3]
                    if bits_list[person]==1:#本当
                        if Y[person][i]==1 and bits_list[X[person][i]-1]==1:
                            pass
                            # print("OK1",Y[person][i],person,flag)
                        elif Y[person][i]==0 and bits_list[X[person][i]-1]==0:
                            pass
                            # print("OK1",Y[person][i],person,flag)
                        else:
                            flag=False
                            # print("NG",Y[person][i],person,flag)
                            break
                    else:#嘘人
                        if Y[person][i]==1 and bits_list[X[person][i]-1]==0:
                            pass
                            # print("OK1",Y[person][i],person,flag)
                        elif Y[person][i]==0 and bits_list[X[person][i]-1]==1:
                            pass
                            # print("OK1",Y[person][i],person,flag)
                        else:
                            flag=False
                            # print("NG",Y[person][i],person,flag)
                            break
            if flag==False:
                break
        if flag==False:
            break
    if flag==True:
        num_people=sum(x==1 for x in bits_list)
        bef=max(num_people, bef)
print(bef)

















