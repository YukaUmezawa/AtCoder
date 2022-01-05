NUM="1222"#input()
A=int(NUM[0])
B=int(NUM[1])
C=int(NUM[2])
D=int(NUM[3])
result=0
while result!=7:
    if A +B +C +D==7:
        op=["+","+","+"]
        break
    if A +B +C -D==7:
        op=["+","+","-"]
        break
    if A +B -C +D==7:
        op=["+","-","+"]
        break
    if A +B -C -D==7:
        op=["+","-","-"]
        break
    if A -B +C +D==7:
        op=["-","+","+"]
        break
    if A -B +C -D==7:
        op=["-","+","-"]
        break
    if A -B -C +D==7:
        op=["-","-","+"]
        break
    if A -B -C -D==7:
        op=["-","-","-"]
        break
print("{}{}{}{}{}{}{}=7".format(A,op[0],B,op[1],C,op[2],D))
