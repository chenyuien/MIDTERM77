info = {"123 456":9000,"456 789":5000,"789 888":6000,"336 558":10000,"775 666":12000,"566 221":7000}
a = int(input("輸入查詢組數 N 為:"))
for i in range(a):
    a_p = input()
    if a_p in info:
        print(info[a_p])
    else:
        print("error")