from itertools import combinations

N, M = map(int,input().split())
if M==0:
    print(1)
else:
    xy = [map(int, input().split()) for _ in range(M)]
    x, y = [list(i) for i in zip(*xy)]



    ans=1
    flag2=False
    for k in range(N+1,1,-1):
        # flag=True
        # if flag2==True:
        #         break
        for comb in combinations(range(1,N+1,1),k):
            flag=True
            if flag2==True:
                break
            # print("comb:"+str(comb))#(1, 2, 3, 4, 5) <class 'tuple'>

            for c in combinations(comb,2):
              # print("c:"+str(c))

              former_index=[i for i, x_ in enumerate(x) if x_ == c[0]]
              latter_index=[i for i, y_ in enumerate(y) if y_ == c[1]]
              l1_l2_and=set(former_index)&set(latter_index)
              # print("former_index:"+str(former_index))
              # print("latter_index:"+str(latter_index))
              # print("set(former_index):"+str(set(former_index)))
              # print("set(latter_index):"+str(set(latter_index)))
              # print("l1_l2_and:"+str(l1_l2_and))
              # print("ans0:"+str(ans))
              if len(l1_l2_and)==0:
                flag=False
                break
              # print("len(comb)"+str(len(comb)))
              # print("ans1:"+str(ans)+"comb:"+str(comb))
              # flag2=True
            if ans<len(comb) and flag==True:
                ans=len(comb)
                # print("ans:"+str(ans)+"comb:"+str(comb))
                flag2=True

    print(ans)




