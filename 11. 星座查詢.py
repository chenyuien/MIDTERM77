month,day = input("輸入月及日為:").split()
if month == "01":
    if int(day) >= 21: print("星座為:Aquarius")
    else: print("星座為:Capricorn")
elif month == "02":
    if int(day) <= 18: print("星座為:Aquarius")
    else: print("星座為:Pisces")
elif month == "03":
    if int(day) <= 20: print("星座為:Pisces")
    else: print("星座為:Aries")
elif month == "04":
    if int(day) <= 20: print("星座為:Aries")
    else: print("星座為:Taurus")
elif month == "05":
    if int(day) <= 21: print("星座為:Taurus")
    else: print("星座為:Gemini")
elif month == "06":
    if int(day) <= 21: print("星座為:Gemini")
    else: print("星座為:Canser")
elif month == "07":
    if int(day) <= 22: print("星座為:Canser")
    else: print("星座為:Leo")
elif month == "08":
    if int(day) <= 23: print("星座為:Leo")
    else: print("星座為:Virgo")
elif month == "09":
    if int(day) <= 23: print("星座為:Virgo")
    else: print("星座為:Libra")
elif month == "10":
    if int(day) <= 23: print("星座為:Libra")
    else: print("星座為:Scorpio")
elif month == "11":
    if int(day) <= 22: print("星座為:Scorpio")
    else: print("星座為:Sagittarius")
elif month == "12":
    if int(day) <= 21: print("星座為:Sagittarius")
    else: print("星座為:Aquarius")