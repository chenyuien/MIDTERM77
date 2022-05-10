test,student = map(int,input("請輸入考試次數及學生數:").split())
percentage = list(map(eval,input("每次考試所佔的比率:").split()))
total = []
for i in range(student):
    score = list(map(int,input().split()))
    num = 0
    for j in range(len(score)):
        num += score[j]*percentage[j]
    total.append(num)
print("全班的總平均值為:%.2f"%(sum(total)/student))