print("*************************************")
print("This solution calculates ages in 2025")
print("*************************************")


#Receive user's age input
age = int(input("How old are you? "))

#Assume the current year is 2023 and the expected year of age is 2050
CURRENT_YEAR = 2023
EXPECTED_YEAR = 2050

#Computed difference of age in 2050 from current year
DIFF_YEAR = EXPECTED_YEAR - CURRENT_YEAR

#Calculated result of age in 2050
result = age + DIFF_YEAR

#Displayed output of results
print(f"\nIn {EXPECTED_YEAR}, you will be {result} years old.")
