print("=====EXPENSE CALCULATOR=====")
food = float(input("Enter food expense:Rs."))
transport = float(input("Enter transport expense:Rs."))
snacks = float(input("Enter snacks expense:Rs."))
total = food + transport + snacks
print("\n=====EXPENSE SUMMARY =====")
print("Food expense:Rs.",food)
print("Transport expense:Rs.",transport)
print("Snacks expense:Rs.",snacks)
print("---------------")
print("Total expense:Rs.",total)
average = total / 3
print("Average expense:Rs.",average)
average = total / 3
print(f"Average expense:Rs.{average:.2f}")

