NUM=input()
def func(i,total):
    if i==3:
        if total==7:
            print()
    func(i+1,total+int(NUM[i+1]))
    func(i+1,total-int(NUM[i+1]))
func(0,int(NUM[0]))