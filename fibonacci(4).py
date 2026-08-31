# Fibonacci using recursion
def fibonacci(n):
    if n<=1:
        return n 
    return fibonacci (n-1) + fibonacci(n-2)
n = int(input("Enter number of terms:"))

for i in range(n):
    print (fibonacci(i),end=" ")
 
 
 
   
# Fibonacci using for loop
n = int(input("Enter number of terms :"))

a = 0
b = 1

for i in range (n):
    print (a,end = " ")
    a, b= b, a + b 
 
 
 
   
#Fibonacci without function 
a = 0
b = 1
for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c 
      
