minute,second = map(int,input("請輸入遊戲時間：").split(":"))
time = minute*60+second
time -= 75
z = 1
x = 0
while time > 0:
    if z % 3 == 0:
        x += 7
        if z % 2 == 0:
            x -= 1
    else:
        x += 6
        if z % 2 == 0:
            x -= 1
    z += 1
    time -= 30
print(f"{x} 隻兵")