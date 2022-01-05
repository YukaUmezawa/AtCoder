N,M=map(int,input().split())
if M==0:
    print(N)
else:
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]
    connections=[[]]*N
    #print(connections)

    #print(done)
    # j=0
    # for i in range(N):
    #     con=[]
    #     #j=i
    #     while A[j]==i+1:
    #       con.append(B[j])
    #       j+=1
    #       if j>=M:
    #         break
    #k=0
    for i in range(N):
        con=[]
        for j in range(M):
            if A[j]==i+1:
                con.append(B[j])
        #k=j+1

          #print(con)
        connections[i]=con
        #print(connections)
    #print(connections)
    def search(node):
        if node is None:
            return
            #print(count)
        # for i in i.connect:
        for k in connections[node-1]:
            if done[k-1]==0:
                done[k-1]=1
                search(k)
          #print(k,node)
        return

    c=0
    for i in range(N):
      done=[0]*N
      search(i+1)
      done[i]=1
      c+=sum(done)
      #print(done,c)
    print(c)