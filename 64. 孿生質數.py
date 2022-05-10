def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

a = int(input("請輸入第一個要判斷的數字："))
b = int(input("請輸入第二個要判斷的數字："))
if b != a+2:
    print("N")
else:
    if prime(a):
        if prime(b):
            print("Y")
        else:
            print("N")
    else:
        print("N")