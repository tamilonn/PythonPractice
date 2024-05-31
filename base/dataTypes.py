num = 10
long = 1001
float = 10.5
string = "Tamilselvan"

char = 'A'


print(num)
print(long)
print(float)
print(string)
print(char)

#addition
num1 = 10
num2 = 55
sum= num1 + num2
print("addition is " + str(sum)) 

sub = num2 - num1
print("subtraction is " + str(sub)) 


mul = num1 * num2
print("multiplication is "+ str(mul))

div = num2 / num1
print("division is "+ str(div))

str1 = 'a'
str2 = 'a'

print (str1 != str2)

print(str1 is str2)

'-------------------------------------'

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

  '-----------------------------------------------'

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
