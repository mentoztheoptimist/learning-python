# coffee menu system

print ("Welcome to sorrow Coffee Shop ")
print ("Lets customize your coffee order")

#step 1 choosing a size
Coffee_Size = input ("pick a size Small, Medium, Large: ").lower()
print (f"I see you want a {Coffee_Size} Coffee!")

#step 2 choose a coffee flavor
Coffee_Flavor = input ("pick a coffee flavor Strawberrry, Milk, Chocolate, ube, caramel: ").lower()
print (f"I see you want a {Coffee_Flavor} Coffee!")


Coffee_Toppings = input (" What toppings do u want? Strawberry, BlueBerries, Oreos, Or Sprinkles ").lower()
print (f"Added {Coffee_Toppings} on your coffee")


#step 3 sugar or nah?
Sugar = input("do u want sugar or not? YES OR NO?: ").lower()
if Sugar == "Yes":
    print (" Added some sugar ")
elif Sugar == "No":
     print ("Sugar Not Added")

#order suggestion
print ("Your order is ready!")
print (f"Your {Coffee_Size} {Coffee_Flavor} Coffee with {Coffee_Toppings} and {'sugar' if Sugar == 'yes' else 'no sugar'} is ready!")