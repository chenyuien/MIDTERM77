a,b = input("輸入矩陣的維度:").split()
x,y = [],[]
for i in range(int(a)):
    z = list(map(int,input().split()))
    x.append(z)
for i in range(int(a)):
    z = list(map(int,input().split()))
    y.append(z)

# 方法一 -> numpy
import numpy as np
c = np.array(x)
d = np.array(y)
e = c*d
for i in e:
    for j in i:
        print(j,end=" ")
    print()

# 方法二
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         p = x[i][j] * y[i][j]
#         print(p)