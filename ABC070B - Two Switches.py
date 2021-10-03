A,B,C,D=map(int,input().split())

if C>=A:
    if B>=C:
        start=C
        fin=min(B,D)
    else:
        start=0
        fin=0
else:
    if B>=C:
      if B>=D:
        if A>=D:
          start=0
          fin=0
        else:
          start=A
          fin=D
      else:
        start=A
        fin=B
    else:
        start=A
        fin=min(B,D)
print(fin-start)