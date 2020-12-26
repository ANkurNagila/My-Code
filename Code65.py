number = 0
while True:
    try:
        if ((i := int(input("Input a number: "))) != 1):
            number = i
            break
    except ValueError as e:
        print("Enter a valid number! Error:", e)
print(number)
