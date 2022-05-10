s1 = input("sA:")
s2 = input("sB:")
a = ""
b = []

# 取得所有子字串
for i in range(len(s2)):
    for j in s2[i:]:
        a += j
        b.append(a)
    a = ""

if s1 in b:
    print("子字串判斷為: YES")
else:
    print("子字串判斷為: NO")