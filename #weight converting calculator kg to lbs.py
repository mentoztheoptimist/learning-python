#weight converting calculator kg to lbs
"""pounds = 2.20462 #a kilogram is lbs2.20462

Convert_kilograms = float(input("Kilograms?: "))
converted = Convert_kilograms * pounds
print (f"your kilograms in lbs is {round(converted, 1)}") """


#weight converting asking if KG or lbs
"""unit = input("Kilograms or lbs: ")

if unit in ["Kilograms", "kilo", "kg", "kilos", "KG"]:
    weight = float(input("Enter weight in kilograms: "))
    unit2= weight * 2.20462
    converted = "lbs"
elif unit in ["lbs", "pounds", "lbs"]:
    weight = float(input("Enter weight in pounds: "))
    unit2 = float(weight) / 2.20462
    converted = "kg"
else:
    print (f"{unit} is not a valid unit")
    
print (f"your weight is {round(unit2 , 1)} {converted} ")"""