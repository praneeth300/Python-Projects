#The body mass index or BMI is calculated from weight and height of a person

Height=float(input('Enter you height is cm'))
weight=float(input('Enter you weight in kg'))
Height= Height/100
BMI=weight/(Height* Height)
print('Your Body masss index is:',BMI)
if (BMI>0):
    if(BMI<=16):
        print('Your are severly underweight')
    elif(BMI<=18.5):
        print('Your are underweight')
    elif(BMI<=25):
        print('Your are healthy')
    elif(BMI<=30):
        print('Your are overweight')
    else:
        print('Your severly overweight')
else:('Enter valid details')