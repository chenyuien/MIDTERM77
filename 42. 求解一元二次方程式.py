a = int(input())
b = int(input())
c = int(input())

# 方法一 -> numpy
# import numpy
# z = numpy.roots([a,b,c])
# print(int(z[1]))
# print(int(z[0]))

# 方法二
z = b**2 - 4*a*c
if z > 0:
    x = (-b + pow(b**2 - 4*a*c,0.5))/(2*a)
    y = (-b - pow(b**2 - 4*a*c,0.5))/(2*a)
    print(int(x))
    print(int(y))
elif z == 0:
    x = -b / (2*a)
    print(int(x))
else:
    print("無解")
