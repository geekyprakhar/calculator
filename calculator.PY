num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
sum = num1+num2
subtract = num1-num2
product=num1*num2
modulous =num1%num2
exponent =num1**num2
floordivision =num1//num2
print('**************************************************************')
print('okay here is your answer baby')
print('**************************************************************')
a=input('enter the operator')
if (a=='+'):
   print('The sum is ', sum)
elif (a=='-'):
   print('The subtract is',subtract)
elif (a=='*'):
   print('The product is', product)
elif (a=='%'):
   print('The modulous is ', modulous)
elif (a=='**'):
   print('The exponent is ', exponent)
elif (a=='//'):
   print('The floor division is ', floordivision)
