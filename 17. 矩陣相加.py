_list = []
end = False
for i in range(2):
    if i == 1:  # 透過第二個矩陣大小是否與第一個矩陣大小相同, 來判斷是否能相加 (缺點 -> 輸入矩陣個數必須與輸入的大小相同, 否則找不出錯誤)
        if input() != size:  # 只適用於比較情況 (不需變數)
            end = True
    else:
        size = input() # 輸入矩陣大小
    for j in range(int(size[0])):
        sub_array = list(map(int,input().split()))  # 輸入矩陣元素 (個數必須與 size 值相同)
        _list.append(sub_array)

if end:
    print("兩個矩陣無法相加")
    exit()

# add
ans_list = []
for i in range(len(_list)//2):
    ans_sub_list = []
    for j in range(len(_list[i])):
        ans_sub_list.append(_list[i][j] + _list[i+len(_list)//2][j])
    ans_list.append(ans_sub_list)

# print()
print("-----")
for i in ans_list:
    for j in i:
        print(j,end=" ")
    print()