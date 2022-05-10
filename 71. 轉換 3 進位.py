ten = int(input("請輸入十進位的正整數："))
x,y = divmod(ten,3)
ans = str(y)
while x >= 3:
    x,y = divmod(x,3)
    ans += str(y)
if x != 0:
    ans += str(x)
print(f"{ten} 的三進位為 {ans[::-1]}")