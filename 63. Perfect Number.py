n = int(input("請輸入正整數n："))
b = []
for i in range(1,n):
    if n % i == 0:
        b.append(i)
if sum(b) == n:
    print("perfect")
else:
    if sum(b) > n:
        print("abundant")
    else:
        print("deficient")