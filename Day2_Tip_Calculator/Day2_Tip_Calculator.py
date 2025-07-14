# Output: Welcome Message
print("Welcome to the tip calculator!")

# Input: what was the total bill? (float - rounded to 2 decimal places)
total_bill = float(input("what was the total bill?\n"))
total_bill = round(total_bill, 2)

# Input: How much tip would you give? in (int)
tip = int(input("How much tip would you give?\n"))

# Input: How many people will split the bill? (int)
people_split = int(input("How many people will split the bill?\n"))

# Output: Each person should pay ...
each_person_pay = (total_bill + tip)/people_split
each_person_pay = round(each_person_pay, 2)

print(f"Each person should pay: ${each_person_pay}")