num_list = list(map(int,input().split(",")))
c_factor = []

# 方法一 numpy
# import numpy as np
# for i in range(len(num_list)):
#     for j in range(i+1,len(num_list)):
#         c_factor.append(np.gcd(num_list[i],num_list[j]))
# print(max(c_factor))

# 方法二
def find_factor(x):
    factor = []
    for i in range(1,x+1):
        if x % i == 0:
            factor.append(i)
    return factor

for i in range(len(num_list)):
    f1 = find_factor(num_list[i])  # 找出 i 的因數
    for j in range(i+1,len(num_list)):
        f2 = find_factor(num_list[j])  # 找出 j 的因數
        for k in (f1+f2):
            if (f1+f2).count(k) == 2:  # 找出 i,j 的公因數
                c_factor.append(k)
print(max(c_factor))