def append_list(x):  # 將花色與數字個別加入 list
    a,b = [],[]
    for i in x:
        a.append(i[0])
        b.append(i[1])
    return a,b

def sequence(x):  # 判斷是否為順子
    for i in x:
        try:  # IndexError: list out of range
            if int(x[x.index(i)+1]) - int(i) != 1:
                return False
        except:
            pass
    return 5

def same_color(x,z):  # 判斷是否為同花順
    y = x[0]
    for i in x:
        if i != y:
            return False
    return sequence(z) + 3
        
def remain_card_type(x):  # 剩餘牌型
    if x.count(4) == 4 and x.count(1) == 1:
        return 7
    elif x.count(2) == 2 and x.count(3) == 3:
        return 6
    elif x.count(3) == 3 and x.count(1) == 2:
        return 4
    elif x.count(2) == 4 and x.count(1) == 1:
        return 3
    elif x.count(2) == 2 and x.count(1) == 3:
        return 2
    elif x.count(1) == 5:
        return 1

def judge(x,y,z):  # 判斷牌型
    hc = same_color(x,y)
    if hc == False:
        hc = sequence(y)
        if hc == False:
            hc = remain_card_type(z)
    return hc

p = 0
while p != -1:
    first = input().split()
    second = input().split()
    f_flower,f_num = append_list(first)
    s_flower,s_num = append_list(second)
    f_count,s_count = [],[]

    # get count
    for i in f_num:
        f_count.append(f_num.count(i))
    for i in s_num:
        s_count.append(s_num.count(i))

    # 判斷牌型
    hand_card = judge(f_flower,f_num,f_count)
    non_hand_card = judge(s_flower,s_num,s_count)
    
    if hand_card > non_hand_card:
        print(1)
    else:
        print(0)
    
    p = int(input())