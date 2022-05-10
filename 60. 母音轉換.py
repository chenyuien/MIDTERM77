a = input("請輸入一串小寫英文:")
b = ["a","e","i","o","u"]
ans = ""
for i in a:
    if i in b:
        ans += "."
    else:
        ans += i
print(ans)