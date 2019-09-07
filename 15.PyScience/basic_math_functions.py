import math

# value of PI
print(math.pi)
# value of e
print(math.e)
# absolute value...
positive_value = 98.6 
negative_value = -271.1
print("Abs of %.2f is %.2f" %(positive_value, math.fabs(positive_value)))
print("Abs of %.2f is %.2f " %(negative_value, math.fabs(negative_value)))
# floor and ceild of decimal numbers...
print("Floor of %.2f is %.2f" %(positive_value, math.floor(positive_value)))
print("Floor of %.2f is %.2f" %(negative_value, math.floor(negative_value)))
print("Ceil of %.2f is %.2f" %(positive_value, math.ceil(positive_value)))
print("Ceil of %.2f is %.2f" %(negative_value, math.ceil(negative_value)))
# factorials...
print ("Factorial of %d is %d" %(0, math.factorial(0)))
print ("Factorial of %d is %d" %(1, math.factorial(1)))
print ("Factorial of %d is %d" %(2, math.factorial(2)))
print ("Factorial of %d is %d" %(3, math.factorial(3)))
print ("Factorial of %d is %d" %(10, math.factorial(10)))
# logarithms...
print ("Logarithm of %.1f is %.1f" %(1.0, math.log(1.0)))
print ("Logarithm of %f is %.1f" %(math.e, math.log(math.e)))
print ("Logarithm base 2 of %.1f is %.1f" %(8, math.log(8,2)))
# pows...
print ("%d^%d is %d" %(2, 3, math.pow(2,3)))
# squares..
print ("Square of %d is %f" %(100, math.sqrt(100.0)))
# rad to degrees and vice-versa...
print ("%.1f degrees are %f radians" %(180.0, math.radians(180.0)))
print ("%f radians are %.1f degrees" %(math.pi, math.degrees(math.pi)))
# imaginary numbers...
print(8j)
print((3 + 2j))
print(1j * 1j)