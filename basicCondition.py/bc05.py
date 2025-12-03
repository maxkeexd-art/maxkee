i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("------------------------------")
number = 0

while number <= 10:
    if number % 2 != 0:
        print(number)
    number += 1
print("------------------------------")
number1 = 0

while number1 <= 10:
    number1 += 1
    if number1 % 2 == 0:
        continue
    print(number1)