two,one = [],[]
for i in range(3):
    a = list(map(int,input("").split()))
    two.append(a)
    one += a
total = 0
num_list = []
for i in range(3):
    total += max(one)

    # 找出 max(one) 在 two 中的 index
    for j in two:
        for k in j:
            if max(one) == k:
                num_list.append((two.index(j)+1,j.index(k)+1))

    one[one.index(max(one))] = 0

print(f"\n最大值為:{total}")
print("位置為",end="")
for i in num_list:
    if i == num_list[-1]:
        print(i)
    else:
        print(i,end=",")