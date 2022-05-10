n,m = map(int,input("輸入 N 及 M 為:").split())
array_list = []

# 建立串列
for i in range(n):
    row = input(f"\n輸入矩陣數值第 {i+1} 列為:").split()
    array_list.append(row)

# 方法 1 -> numpy
# # list to array
# import numpy as np
# a_array = np.array(array_list)

# # output
# x = 1
# for i in a_array.T:
#     print(f"\n輸出矩陣數值第 {x} 列為:",end="")
#     for j in i:
#         print(j,end=" ")
#     print()
#     x += 1

# 方法 2
z = []
y = []
x = 1
for i in range(len(array_list[0])):
    for j in range(len(array_list)):
        z.append(array_list[j][i])
    y.append(z)
    z = []
for i in y:
    print(f"\n輸出矩陣數值第 {x} 列為:",end="")
    for j in i:
        print(j,end=" ")
    print()
    x += 1