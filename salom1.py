filename,operation=map(str,input("Аввал номи ва баъди пробел намуди  операчсияро дохил кунед").split())
data=[]
with open (filename) as f:
    for line in f:
        data.append([int(x) for x in line.split()])
print(data)
data2=[]
for i in data:
    for j in range(1):
        summa=i[0]+i[1]
        data2.append(summa)
for i in data2:
    i
print(data2)