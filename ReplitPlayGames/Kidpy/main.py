from kidpy import *

clearscreen()
write('Hello world!')
say('Hello world!')
num1 = add(200, 10)
num2 = take(num1, 10)
div1 = divide(num1, num2)
multiply1 = multiply(div1, num2)
power1 = power(8, 3)
sqrt1 = sqareroot(25)
write(num1)
write(num2)
write(div1)
write(multiply1)
write(power1)
write(sqrt1)
while True:
    print('Do you want to exit?(y/n) ')
    if get_key('y'):
        print('Ok... ')
        break
    else:
        break

