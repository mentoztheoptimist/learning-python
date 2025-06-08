#numero1 = 5
#numero1 = str(numero1)
#print (numero1 + "50")

#i want to make a code where everyone gets an addition grade

grade = float(input("what is your grade: "))
if grade > 100:
    print("Grade cannot be more than 100.")
else:
    Addedgrade = 5
    final_grade = grade + Addedgrade
    print(f"You got an added grade of +5, so if your original grade is {grade}, your final grade is {final_grade}.")
