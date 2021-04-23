filename=input()
operation=input()
data=[]
data2=[]
with open(filename) as f:
    for line in f:
        data.append([int(x) for  x  in line.split()])
for  i in data:
    for j in i:
        data2.append(j)
print(data2)