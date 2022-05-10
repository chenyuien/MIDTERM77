num = int(input("輸入筆數 n:"))
a = {}
for i in range(num):
    eg,ch = input().split()
    a[eg] = ch
check = input("輸入欲查詢單字:")
if check in a:
    print(f"{check}中文意思為{a[check]}")
else:
    print("字典未有此單字")