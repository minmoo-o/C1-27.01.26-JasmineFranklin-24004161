numbers = [1, 2, 3, 4]

result = 1

for item in numbers:
    if type(item) == int or type(item) == float:
        result = result * item

print(result)
