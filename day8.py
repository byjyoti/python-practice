while True:
    try:
        age = int(input("Enter your age:"))
        print("Next year you will be",age + 1)
        break
    except ValueError:
        print("Please enter numbers only")



