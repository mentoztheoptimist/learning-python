#python compound interest calculator

principle = 0
rate = 0    
time = 0

while principle <= 0:
    principle = float(input("Enter principle amount in dollars: "))
    if principle <= 0:
        print ("Principle cannot be less than or equal to zero")

while rate <= 0:
    rate = float(input("enter interest rate amount: "))
    if rate <= 0:
        print ("rate cannot be less than or equal to zero")

while time <= 0:
    time = int(input("enter time in years: "))
    if time <= 0:
        print ("time cannot be less than or equal to zero")
        
Total_Amount = principle * pow((1 + rate / 100), time)
print(f"your total amount is ${Total_Amount} after {time}year/s")
        
