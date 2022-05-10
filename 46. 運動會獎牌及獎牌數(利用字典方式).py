num = int(input("輸入比數 n:"))

a = {}
for i in range(num):
    name,value = input().split()
    a[name] = value
for i in a:
    print(f"{i}牌得到 {a[i]} 面")