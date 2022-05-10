num = input("輸入整數數列(end結束):")
while num != "end":
    num_list = []
    for i in range(len(num)):
        for j in range(i,len(num)):
            # 判斷迴文
            if len(num[i:j+1]) > 1:
                if num[i:j+1] == num[i:j+1][::-1]:
                    num_list.append(num[i:j+1])
    # 找出最長子數列
    a = "0"
    for i in num_list:
        if len(i) > len(a):
            a = i
        elif len(i) == len(a):
            if int(i) < int(a):
                a = i
    print(f"最長迴文數字子數列為:{a}")
    num = input("輸入整數數列(end結束):")
print("結束")
    