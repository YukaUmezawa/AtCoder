
S="125"#input()

def func(s,i):
    if i==len(S)-1:
        return sum(list(map(int,s.split("+"))))
    return func(s+S[i+1],i+1) + func(s + "+" + S[i+1],i+1)

ans=func(S[0],0)
print(ans)














