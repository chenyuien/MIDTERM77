m = int(input("請輸入階層值 M："))
n = 1
num = 1
while num < m:
    n += 1
    num *= n
print(f"超過 M 為{m}的最小階層 N 值為：{n}")