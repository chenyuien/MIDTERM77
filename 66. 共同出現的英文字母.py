a = set(list(input("請輸入string_a：")))
b = set(list(input("請輸入string_b：")))
common = list(a) + list(b)
str_dict = {}
for i in common:
    if common.count(i) == 2:
        if i not in str_dict.values():
            str_dict[ord(i)] = i
z = sorted(str_dict.keys())  # 以 key 值排序
if not z:
    print("N")
else:
    for i in z:
        print(str_dict[i],end="")