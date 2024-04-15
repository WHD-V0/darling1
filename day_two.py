names = ['yuanhua','lidan','liulian']
for name in names:
    print(name)

for number in range(1,6):
    print(number)
number_list = list(range(1,8,2))
print(number_list)

squ = []
for value in range(1,10):
    squ.append(value**2)
print(squ[1:5:2])

print(sum(squ))

num = list(range(2,14,2))
num_2 = num[:]
num_2.append(19)
num.append(17)
print(num_2)
print(num)

dimention = (200,100)
for dim in dimention:
    print(dim)
