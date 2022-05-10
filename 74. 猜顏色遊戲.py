ans = ["red","blue","red","green"]
chance = 0
while chance != 10:
    hint = ""
    color_list = input().split()
    for i in range(len(color_list)):
        if color_list[i] in ans:
            if color_list[i] == ans[i]:
                hint += "1"
            else:
                hint += "2"
        else:
            hint += "3"
    if hint == "1111":
        print("正確答案")
        exit()
    print(hint)
    chance += 1
print("挑戰失敗")