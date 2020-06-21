n=int(input())
A=[]
B=[]
for i in range(n):
    if n-i>=0:
        A.append(i)
    if n-3*i>=0:
        B.append(2*i)
    n=n-3*i
    if n<0:
        break
if len(A)==len(B):
    if n-(len(A)+B[len(B)-1])<=(A[len(A)-1]+1):
        print("Bob")
    else:               
        print("Nelson")
else:
    print("Nelson")