first = input("輸入第一行正整數為:")
second = input("\n第二行中數列中的數字為:").split()
count = 1
for i in second:
    if second.count(i) > count:
        count = second.count(i)
        num = i
if count == 1:
    print("每個數字剛好只出現 1 次")
else:
    print(f"最大出現次數的數字為:{num}\n\n出現次數為{count}")