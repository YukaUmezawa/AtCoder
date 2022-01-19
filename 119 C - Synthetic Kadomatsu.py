# N,A,B,C=map(int, input().split())
# l = []
# #リストlにappend()を使って格納していく
# for _ in range(N):
#     l.append(int(input()))

# from itertools import combinations
# import numpy as np

# # diff_sum_old=np.inf
# mp_sum_old=np.inf
# for i in range(1,N-1):
#     for a in combinations(l,i):
#         a_sum=sum(a)
#         diff_a=abs(A-a_sum)
#         combi_a=(i-1)*10
#         mp_a=diff_a+combi_a
#         l_remain=[s for s in l if s not in a]
#         len_l=len(l_remain)

#         for j in range(1,len_l):
#             for b in combinations(l_remain,j):
#                 b_sum=sum(b)
#                 diff_b=abs(B-b_sum)
#                 combi_b=(j-1)*10
#                 mp_b=diff_b+combi_b
#                 l_remain2=[s for s in l_remain if s not in b]
#                 len_l2=len(l_remain2)

#                 for k in range(1,len_l2+1):
#                     for c in combinations(l_remain2,k):
#                         c_sum=sum(c)
#                         diff_c=abs(C-c_sum)
#                         combi_c=(k-1)*10
#                         mp_c=diff_c+combi_c

#                         mp_sum=mp_a+mp_b+mp_c
#                         if mp_sum<mp_sum_old:
#                             mp_sum_old=mp_sum
# print(mp_sum_old)

#                         # diff_sum=diff_a+diff_b+diff_c
#                         # if diff_sum<diff_sum_old:
#                         #     diff_sum_old=diff_sum










N,A,B,C=map(int, input().split())
l = []
#リストlにappend()を使って格納していく
for _ in range(N):
    l.append(int(input()))

from itertools import combinations
import numpy as np
# print("l",l)
# diff_sum_old=np.inf
mp_sum_old=np.inf

def removed(taisyou_l,rmv_l):
  for i in rmv_l:
    taisyou_l.remove(i)
  return taisyou_l

for i in range(1,N-1):
    for a in combinations(l,i):
        print("l",l)
        l_rmv=l.copy()
        a_sum=sum(a)
        diff_a=abs(A-a_sum)
        combi_a=(i-1)*10
        mp_a=diff_a+combi_a
        print("a",a)
        #l_rmv.remove(1000)
        l_remain=l_rmv.copy()
        removed(l_remain,a)
        #print("l_remain",l_remain)
        print("l_rmv",l_rmv)
        #l_remain=[s for s in l if s not in [10]]
        len_l=len(l_remain)
        #print("a",a)
        print("l_remain",l_remain)
        print("len_l",len_l)
        for j in range(1,len_l):
            for b in combinations(l_remain,j):
                l_remain2=l_remain.copy()
                b_sum=sum(b)
                diff_b=abs(B-b_sum)
                combi_b=(j-1)*10
                mp_b=diff_b+combi_b
                # l_remain2=[s for s in l_remain if s not in b]
                removed(l_remain2,b)
                len_l2=len(l_remain2)
                print("l_remain",l_remain)
                print("len_l2",len_l2)
                for k in range(1,len_l2+1):
                    for c in combinations(l_remain2,k):
                        c_sum=sum(c)
                        diff_c=abs(C-c_sum)
                        combi_c=(k-1)*10
                        mp_c=diff_c+combi_c

                        mp_sum=mp_a+mp_b+mp_c
                        print(mp_a,mp_b,mp_c,mp_sum)
                        if mp_sum<mp_sum_old:
                            mp_sum_old=mp_sum
print(mp_sum_old)

                        # diff_sum=diff_a+diff_b+diff_c
                        # if diff_sum<diff_sum_old:
                        #     diff_sum_old=diff_sum