s1 = input("輸入 s1 為:")
s2 = input("\n輸入 s2 為:")
a = ""
b = []

# 取得所有子字串
for i in range(len(s2)):
    for j in s2[i:]:
        a += j
        b.append(a)
    a = ""

if s1 in b:
    print("YES")
else:
    print("NO")