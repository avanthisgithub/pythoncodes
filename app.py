#weight converter program
weight = float(input("Enter your weight: "))
unit  = str(input("Have you entered weight in kg or lbs? "))
if unit.lower() == "kg":
    lbs = str(weight * 0.453592)
    print("Your weight in lbs is " + lbs)
elif unit.lower() == "lbs":
    kg = str(weight * 2.20462)
    print("Your weight in kg is " + kg)
else:
    print("error")




