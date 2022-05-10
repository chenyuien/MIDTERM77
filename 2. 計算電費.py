kwh = int(input())
summer, non_summer = 0,0
if kwh <= 120:
    summer += kwh*2.1
    non_summer += kwh*2.1
else:
    summer += 120*2.1
    non_summer += 120*2.1
    if kwh <= 330:
        summer += (kwh-120)*3.02
        non_summer += (kwh-120)*2.68
    else:
        summer += (330-120)*3.02
        non_summer += (330-120)*2.68
        if kwh <= 500:
            summer += (kwh-330)*4.39
            non_summer += (kwh-330)*3.61
        else:
            summer += (500-330)*4.39
            non_summer += (500-330)*3.61
            if kwh <= 700:
                summer += (kwh-500)*4.97
                non_summer += (kwh-500)*4.01
            else:
                summer += (kwh-700)*5.63
                non_summer += (kwh-700)*4.5
print(f"Summer months:{summer}")
print(f"\nNon-Summer months:{non_summer}")