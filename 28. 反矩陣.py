import numpy as np
a = list(map(int,input().split()))
a[1] = -(a[1])
b = list(map(int,input().split()))
b[0] = -(b[0])
z = np.array([a,b])
det = z[0][0]*z[1][1] - z[0][1]*z[1][0]
x = (1/det)*z.T
for i in x:
    for j in i:
        print("%.1f"%j,end=" ")
    print()