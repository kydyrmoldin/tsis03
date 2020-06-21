
A=[]

a=True
while a:
    l=input().split()
    if len(l)==2:
        s,n=l[0],l[1]
    else:
        s=l[0]
    if s=='push':
        A.append(n)
        print("OK")
    if s=="size" :
        print(len(A))
    if s=="pop":
        A.pop()
        print("OK")
    if s=="front":
        print(A[0])
    if s=="back":
        print(A[len(A)-1])
    if s=="clear":
        A.clear()
        print("OK")
    if s=="end":
        a=False
        print("Black Devil")