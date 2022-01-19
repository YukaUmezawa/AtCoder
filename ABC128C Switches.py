from itertools import product
from itertools import combinations

N, M= map(int, input().split())

ks = [list(map(int, input().split())) for l in range(M)]
#ks [[2, 1, 2], [1, 1], [1, 2]]

p = list(map(int, input().split()))

# for bits_switch in product((1,0),repeat=N):
#     # print(bits_list)#(1, 1, 1)'tuple'
#     #light_on=bits_list.count(1)
#     for person in range(M):
#         for connect in ks[i][1:]:
#             if ks[i][connect]:
#                 pass


lst = list(range(1,N+1))
ok=0
flag=True
for i in range(N+1):
    for comb in combinations(lst, i+1):
        # print(comb)# (1,)
        for person in range(M):
            # print("person",person)
            c=0
            for connect in ks[person][1:]:#1 2 5
                # print("ks[i][1:]",ks[person][1:])
                if comb.count(connect):
                    c+=1
                    # print("c",c)
            if c!=0 and c%2==p[person]:
                flag=True
                # print("good")
                pass
            else:
                # print("bad")
                flag=False
                break
        if flag==True:
            ok+=1
            # print(ok)
print(ok)







