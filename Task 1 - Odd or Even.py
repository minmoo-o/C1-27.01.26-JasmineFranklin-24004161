value = input("Please enter a number: ")

try:
    number = float(value)

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

except:
    print("That is not a number")