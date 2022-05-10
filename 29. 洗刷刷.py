# 若數字不相鄰, 即為和
a = input("甲方的數字: ")
b = input("乙方的數字: ")
for i in range(len(a)):
    if a[i] == "1" and b[i] == "5":
        print("贏",end="")
    elif a[i] == "5" and b[i] == "1":
        print("輸",end="")
    elif int(a[i]) == int(b[i]) + 1:
        print("贏",end="")
    elif int(b[i]) == int(a[i]) + 1:
        print("輸",end="")
    else:
        print("和",end="")