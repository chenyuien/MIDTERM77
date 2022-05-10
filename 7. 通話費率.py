month_money,time = map(int,input("輸入月租費型式及通話時間為:").split(","))
if month_money == 186:
    if time * 0.09 > month_money:
        total = time * 0.09 * 0.8
    else:
        total = time * 0.09 * 0.9
elif month_money == 386:
    if time * 0.08 > month_money:
        total = time * 0.08 * 0.7
    else:
        total = time * 0.08 * 0.8
elif month_money == 586:
    if time * 0.07 > month_money:
        total = time * 0.07 * 0.6
    else:
        total = time * 0.07 * 0.7
elif month_money == 986:
    if time * 0.06 > month_money:
        total = time * 0.06 * 0.6
    else:
        total = time * 0.06 * 0.5
print("通話費為：%.0f"%total)