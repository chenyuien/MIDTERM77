# 若解出的數字有複數個, 取第一個取得的數字
password = input("請輸入傳送密碼(6位數): ")
while len(password) < 6:
    password = input("請輸入傳送密碼(6位數): ")
ans = ""
for i in password:
    for j in range(10):
        if j*4%7 == int(i):
            ans += str(j)
            break
print(f"解密後的密碼:{ans}")