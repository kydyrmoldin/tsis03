def podarok(x1, y1, x2, y2, p1, p2):
    if p1>x1 and p1<x2 and y1>p2 and y2<p2:
        print("yes")
    else:
        print("no")
x1, y1, x2, y2, p1, p2 = map(int,input().split())
podarok(x1, y1, x2, y2, p1, p2)