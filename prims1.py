q=[(2,3,1),(5,2,2),(5,3,2),(5,8,2)]
t=[]
g={}
vi=[5,2]
for i in g[vi[-1]]:
    if i[0] not in vi:
        q.append((5,i[0],i[1]))
while(q):
    def fun(x):
        return x[-1]
    q.sort(key=fun)
    if(q[0][1] not in vi):
        vi.append(q[0][1])
        t.append(q[0])
    b=q.pop(0)[1]
    for i in g[b]:
        if(i[0] not in vi):
            q.append((b,i[0],i[1]))