num = int(input("輸入筆數 n:"))
z = []
for i in range(num):
    name = input().split()
    z.append(name)
for i in z:
    print(f"{i[0]}牌得到 {i[1]} 面")