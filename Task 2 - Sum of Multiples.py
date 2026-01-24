a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

total = 0

for i in range(a, b + 1):
    if i % c == 0:
        total += i

print(total)
