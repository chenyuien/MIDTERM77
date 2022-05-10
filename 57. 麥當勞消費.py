def set(x):
    if x == "A":
        return 55
    elif x == "B":
        return 68

main = input("請選擇主餐及升級的套餐：")
drink = input("是否升級成大杯飲料：")
frech = input("是否換成大薯：")
money = 0
if main[0] == "1":
    money += 72 + set(main[1])
elif main[0] == "2":
    money += 62 + set(main[1])
elif main[0] == "3":
    money += 82 + set(main[1])
elif main[0] == "4":
    money += 44 + set(main[1])
elif main[0] == "5":
    money += 60 + set(main[1])
if drink == "是":
    money += 7
if frech == "是":
    money += 13
print(f"總共為 {money} 元")