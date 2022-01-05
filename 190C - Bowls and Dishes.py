# from itertools import combinations

# N, M = map(int,input().split())
# AB = [map(int, input().split()) for _ in range(M)]
# A, B = [list(i) for i in zip(*AB)]
# #A=[1,1,2,3] B=[2,3,4,4]

# K = int(input())
# CD = [map(int, input().split()) for _ in range(K)]
# C, D = [list(i) for i in zip(*CD)]
# # print(C,type(C))

# #1<<3 1000(2) 8
# count_array=[]
# for bit in range(1<<K):
#     put=[]
#     count=0
#     for i in range(K):
#         if bit & 1<<i:
#             put.append(C[i])
#         else:
#             put.append(D[i])
#     # print(put)#[2,3,3]
#     put.sort(reverse=True)
#     put=list(set(put))
#     # print("put"+str(put))
#     for comb in combinations(put, 2):#(2,3)tuple
#         index=[i for i, a in enumerate(A) if a == comb[0]]
#         # print("index:"+str(index))
#         for i in index:
#             if B[i]==comb[1]:
#                 count+=1

#     count_array.append(count)
#     # print("count_array"+str(count_array))



# print(max(count_array))


# from itertools import combinations

# N, M = map(int,input().split())
# AB = [map(int, input().split()) for _ in range(M)]
# A, B = [list(i) for i in zip(*AB)]
# #A=[1,1,2,3] B=[2,3,4,4]

# K = int(input())
# CD = [map(int, input().split()) for _ in range(K)]
# C, D = [list(i) for i in zip(*CD)]
# # print(C,type(C))

# #1<<3 1000(2) 8
# count_array=[]
# for bit in range(1<<K):
#     put=[]
#     count=0
#     for i in range(K):
#         if bit & 1<<i:
#             put.append(C[i])
#         else:
#             put.append(D[i])
#     # print(put)#[2,3,3]
#     put.sort(reverse=True)
#     put=list(set(put))
#     # print("put"+str(put))
#     for comb in combinations(put, 2):#(2,3)tuple
#         index=[i for i, a in enumerate(A) if a == comb[0]]
#         # print("index:"+str(index))
#         for i in index:
#             if B[i]==comb[1]:
#                 count+=1

#     count_array.append(count)
#     # print("count_array"+str(count_array))



# print(max(count_array))


from itertools import combinations
from itertools import product

N, M = map(int,input().split())
AB = [map(int, input().split()) for _ in range(M)]
A, B = [list(i) for i in zip(*AB)]
#A=[1,1,2,3] B=[2,3,4,4]

K = int(input())
CD = [map(int, input().split()) for _ in range(K)]
C, D = [list(i) for i in zip(*CD)]
# print(C,type(C))

# def my_index(l, x, default="False"):
#     if x in l:
#         return True
#     else:
#         return default


#1<<3 1000(2) 8
# count_array=[]
bf_max=0
for bit_set in product((0,1),repeat=K):
    plates=[0]*N
    count=0
    #(0,1,0)
    for index,bit in enumerate(bit_set):
        if bit==1:
            plates[C[index]-1]=1
        else:
            plates[D[index]-1]=1
    for i in range(M):
        if plates[A[i]-1]!=0 and plates[B[i]-1]!=0:
            count+=1

    bf_max=max(count,bf_max)


print(bf_max)























