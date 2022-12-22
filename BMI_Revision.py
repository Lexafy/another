# BMI Calculator

print('This is a BMI calculator')
weight = float(input('Enter your weight in Kg'))
height = float(input('Enter your hight in meters'))
BMI = weight/(height * height)

# Conditions
if(BMI > 0):
    if (BMI <= 16):
        print("You are overweight")
    elif(BMI <= 18.5):
        print("You are underweight")
    elif(BMI <= 25):
        print("Congrats you are healthy")
    elif(BMI<=30):
        print("You are overweight")
    else:
        print("You are very overweight")
else:
    print("Enter valid details")