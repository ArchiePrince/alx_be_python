print("*************************************")
print("This solution calculates ages in 2025")
print("*************************************")


#Receive user's age input

age = input("How old are you?\n")
age = int(age)

CURRENT_YEAR = 2023
EXPECTED_YEAR = 2050

DIFF_YEAR = EXPECTED_YEAR - CURRENT_YEAR

result = age + DIFF_YEAR

print(f"\nIn {EXPECTED_YEAR}, you will be {result} years old.")