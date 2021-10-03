S=input()

T1="dream"
T2="dreamer"
T3="erase"
T4="eraser"

def dream_search(s,i):
    if s[i-1]=="a" and s[i-2]=="e" and s[i-3]=="r" and s[i-4]=="d":
        return True
    else:
        return False

def dreamer_search(s,i):
    if s[i-1]=="e" and s[i-2]=="m" and s[i-3]=="a" and s[i-4]=="e" and s[i-5]=="r" and s[i-6]=="d":
        return True
    else:
        return False

def erase_search(s,i):
    if s[i-1]=="s" and s[i-2]=="a" and s[i-3]=="r" and s[i-4]=="e":
        return True
    else:
        return False

def eraser_search(s,i):
    if s[i-1]=="e" and s[i-2]=="s" and s[i-3]=="a" and s[i-4]=="r" and s[i-5]=="e":
        return True
    else:
        return False

flag=True
start=len(S)-1
while start>=4:
    if S[start]=="m":
        if dream_search(S,start)==True:
            start-=5
        else:
          print("NO")
          flag=False
          break
    elif S[start]=="r":
        if dreamer_search(S,start)==True:
            start-=7
        elif eraser_search(S,start)==True:
            start-=6
        else:
          print("NO")
          flag=False
          break
    elif S[start]=="e":
        if erase_search(S,start)==True:
            start-=5
        else:
          print("NO")
          flag=False
          break
    else:
        print("NO")
        flag=False
        break
if flag==True:
    print("YES")




