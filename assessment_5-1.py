#   1  Division by Zero Error Handle
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
    
    
    
#   2  Invalid Integer Input Handle
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid integer input")    
    
    
#  3  File Not Found Error Handle
try:
    f = open("demo.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File not found")   
    
#   4    Multiple Exception Blocks
try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print( a / b )
except ValueError:
    print("Value Error occurred")
except ZeroDivisionError:
    print("Zero Division Error occurred")
    
 #  5   Finally for Resource Cleanup
try:
    f = open("test.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program ended")
    
              
                        
  #  6    Custom Exception for Invalid Age (<18)                        
age = int(input("Enter age: "))

if age < 18:
    raise Exception("Age must be 18 or above")
else:
    print("Eligible")           
    
 # 7  IndexError when Accessing List
try:
    list1 = [10, 20, 30]
    print(list1[5])
except IndexError:
    print("Index Error occurred")
    
  #  8  Two Numbers Program with All Errors
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# 9  Log Errors to a File
try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)
except Exception as e:
    f = open("error.log", "a")
    f.write(str(e) + "\n")
    f.close()
    print("Error logged to file")
    
                           
 #  10  Email Validation with Exception
email = input("Enter email: ")

if "@" not in email or "." not in email:
    raise Exception("Invalid Email Format")
else:
    print("Valid Email")                                                                       
                                                            