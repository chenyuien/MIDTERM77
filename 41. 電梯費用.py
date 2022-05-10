t = int(input("搭了幾次電梯:"))
floor = 1
money = 0
for i in range(t):
    new_floor = int(input())
    if new_floor > floor:
        money += (new_floor-floor)*20
    elif new_floor < floor:
        money += (floor-new_floor)*10
    floor = new_floor
print(f"{money}元")