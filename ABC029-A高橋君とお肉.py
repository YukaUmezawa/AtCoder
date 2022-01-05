N=int(input())
t=[]
for i in range(N):
    t.append(int(input()))

#Original
# if len(t)==1:
#     print(t[0])
# else:
#     if sum(t)-max(t)<=max(t):
#         print(max(t))
#     else:
#         a1=max(min(t)+max(t), sum(t)-(min(t)+max(t)))
#         a2=sum(t)-max(t)
#         print(min(a1,a2))


#他のアプローチ bit全探索
ans=1000000
for i in range(2**N):
    p1=0
    p2=0
    for j in range(N):
        if (i>>j)&1:
            p1+=t[j]
        else:
            p2+=t[j]
    ans_cand=max(p1,p2)
    if ans_cand<ans:
        ans=ans_cand
print(ans)

#他のアプローチ 再帰
ans=1000000
def func(p1,p2,i):
    global ans
    if i==len(t):
        ans_cand=max(p1,p2)
        ans=min(ans,ans_cand)
        #return ans
    else:
        func(p1+t[i],p2,i+1)
        func(p1,p2+t[i],i+1)

func(0,0,0)
print(ans)



















