# N=int(input())
# S=input()
# # print(S,type(S),S[0])
# c_total=0
# c_total_best=300000
# for i in range(N):
#     c_left=0
#     c_right=0
#     for j in range(i):
#         if S[j]=='W':
#             c_left+=1
#     for k in range(i+1,N):
#         if S[k]=='E':
#             c_right+=1
#     c_total=c_left+c_right
#     if c_total<c_total_best:
#         c_total_best=c_total
#         #print(c_total_best)
# print(c_total_best)
#上述は計算時間に問題あり

N=int(input())
S=input()
c_left_list=[]
c_right_list=[]
c_left=0
c_right=0
result_list=[]
for i in range(N):
    if S[i]=='W':
        c_left+=1
    c_left_list.append(c_left)
for i in reversed(range(N)):
    if S[i]=='E':
        c_right+=1
    c_right_list.append(c_right)
c_right_list.reverse()
# print(c_left_list,c_right_list)
for i in range(N):
    if i==0:
        c_tatal=c_right_list[i+1]
    elif i==N-1:
        c_tatal=c_left_list[i-1]
    else:
        c_tatal=c_left_list[i-1]+c_right_list[i+1]
    result_list.append(c_tatal)
# print(result_list)
print(min(result_list))








