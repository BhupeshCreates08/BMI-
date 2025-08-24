mass = float(input("Enter Your Weight(in kg): "))
height = float(input("Enter Your Height(in meters): "))
bmi = mass/height**2
print("Your BMI is :", round(bmi,2))

#Classification of BMI 

if bmi < 18.5:
    print("You are Underweight.")
elif 18.5 <=bmi< 24.9:
    print("You have a normal Weight")
elif 25 <=bmi< 29.9:
    print("You are Overweight")
else:
    print("You are Obese") 
    


