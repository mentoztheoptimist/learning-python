#Type casting in python
#Type casting is the process of converting one data type to another.

CustomerName = "SpongeBob SquarePants"
CustomerNumber = 100.0
CustomerAge = 26
Is_Customer = True
crabbypatty = 2

#This will print the value of crabbypatty as a string and the boolean value of Is_Customer
'''print (f'crabby_patty is just ${crabbypatty} dollars which is a {bool(Is_Customer)} statement')'''

#else statement to check if the customer paid its order
'''Is_customer_paid = False
Paid = 100
if Paid >= 10:
    print(f'{CustomerName} has not paid the order')
elif Paid == 100:
    print(f'{CustomerName} has paid the order')'''
    
#turn the customerAge into a float value
print (float(CustomerAge))
#if u want to add an arithmetic operation to the float value
print (float(CustomerAge + 10))