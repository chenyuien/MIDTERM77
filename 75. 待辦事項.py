a = input("請輸入事項(若已無事項，請輸入 end)：")
z = []
while a != "end":
    z.append(a)
    a = input("請輸入事項(若已無事項，請輸入 end)：")

for i in z:
    print(f"{z.index(i)+1}. {i}")