km = eval(input("請輸入路程公里數(km)："))
money = 75
b = 0
if km > 1.5:
    a,b = divmod((km-1.5)*1000,250)
    money += a*5
if b:
    money += 5
print(f"所需車資為：{int(money)}")