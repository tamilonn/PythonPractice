data = [100,500,44,5,69]
index = 0
for i in data :
    print(data[index])
    index = index + 1

print("--------------------------------")

print(data)
data.append(21)
print(data)
data.sort()
print(data)
data.clear()
print(data)

print("--------------------------------")


for i in range(1, 10):
    print(i)

for i in range(4, 12, 2):
    print(i)

print("--------------------------------")

for i in range(1,10):
    for j in range(1,10):
        print(i,j)

print("--------------------------------")

a = 10

while a > 0:
    print (a)
    a = a-1