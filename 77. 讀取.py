def output(x,y):
    print(x+"平均：",round(sum(y)/len(y),2))
    print(x+"最大值：",max(y))
    print(x+"最小值：",min(y))

with open("D:\Python\程式設計\練習77題\data.txt","r") as file:
    info = file.readlines()
blood,hreat = [],[]
for i in info:
    z = i.split(". ")
    blood.append(int(z[0]))
    hreat.append(int(z[1].rstrip("\n")))
output("血壓",blood)
print()
output("心跳",hreat)