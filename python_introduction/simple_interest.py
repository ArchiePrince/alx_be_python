print("***************************************************")
print("This solution performs simple interest arithmetic")
print("***************************************************")

#Definition of identifiers

#Principal amount (initial investment)
principal: int = 1000

#Annual interest rate (as decimal)
rate: float = 0.05 #representing 5% annual rate

#Time the money is invested
time: int = 3 # representing 3 years

#Calculating the simple interest earned on an investment over 3 years
interest = principal * rate * time

#Display output
print(f"The simple interest is: {interest}")

