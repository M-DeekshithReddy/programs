'''
a=["school","car","apple","hi"]
b=[]
for i in a:
    b.append(len(i))
c=list(zip(b,a))
c.sort()



'''
a=["school","car","apple","hi"]
a.sort(key=len)
print(a)
