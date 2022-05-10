a = list(input("請輸入A的好友：").split())
b = list(input("請輸入B的好友：").split())
common = a + b
num = 0
for i in common:
    if common.count(i) == 2:
        num += 1
print(int(num/2))