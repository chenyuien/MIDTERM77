def arithmetic(q):
    for i in range(len(q)):
        try:
            if int(q[i+1]) - int(q[i]) != int(q[1]) - int(q[0]):
                return False
        except:
            pass
    return True

def geometric(q):
    for i in range(len(q)):
        try:
            if int(q[i+1]) / int(q[i]) != int(q[1]) / int(q[0]):
                return False
        except:
            pass
    return True

time = int(input())
num_list = []
for i in range(time):
    for j in range(4):
        num = input()
        num_list.append(num)
    # 判斷等差
    if arithmetic(num_list):
        print(" ".join(num_list),"\n此為等差數列")
    # 判斷等比
    if geometric(num_list):
        print(" ".join(num_list),"\n此為等比數列")
    num_list = []