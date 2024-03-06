"""
Alexander Hunt
EECE 2140
Professor Fatema Nafa
March 5, 2024
"""
class BasicMathOperations:   
    def greetUser(self, forename, surname):
        print("Hello, "+forename+" "+surname+".")
        
    def addNumbers(self, num1, num2):
        result = num1+num2
        return result
    
    def performOperation(self, num1, num2, operator):
        if operator == "+":
            result = num1+num2
            return result
        elif operator == "-":
            result = num1-num2
            return result
        elif operator == "*":
            result = num1*num2
            return result
        elif operator == "/" and num2 != 0:
            result = num1/num2
            return result
        elif operator == "/" and num2 == 0:
            print("Error: Unable to divide by zero.")
        else:
            print("Error: Invalid operator.")
            
    def calculate_square(self, num):
        result = num*num
        return result
    
    def factorial(self, num):
        if num>0:
            result=1
            for i in range (1, num+1):
                result *= i
            return result
        else:
            print("Error: Factorial only defined for positive integers.")
            
    def countNumbers(self, num1, num2):
        if num1>num2:
            for i in range (num1, num2+1):
                print(i)
        elif num2>num1:
           for i in range (num1, num2-1, -1):
               print(i)
        else:
            print("Error: Unable to count when numbers are equal.")
    
    def findHypotenuse(self, side1, side2):
        result = (self.calculate_square(side1)+self.calculate_square(side2))**(1/2)
        print(result)
        return result
    
    def findArea(self, side1, side2):
        if type(side1) and type(side2) != str():
            result = side1*side2
            return result
        else:
            result = side1+side2
            return result
        
    def computePower(self, base, exponent):
        result = base**exponent
        return result
    
    def findType(self, argument):
        result = type(argument).__name__
        return result

def main():
    end = False
    while end == False:
        print("Welcome to the python calculator tool.")
        print("                                      ")
        print("Please enter one of the number next to the functions below to select it:")
        print("1 - Greet User")
        print("2 - Add Numbers")
        print("3 - Perform Basic Arithmetic Operations")
        print("4 - Calculate Square of Number")
        print("5 - Calculate Factorial of Integer")
        print("6 - Count Numbers")
        print("7 - Find Hypotenuse of Right Triangle")
        print("8 - Find Area of Rectangle")
        print("9 - Compute Power of a Number")
        print("10 - Return Datatype of Input")
        option = input()
        
        if option == 1:
            forename = input("Please input your name")
            surname = input("Please enter your surname")
            BasicMathOperations.greetUser(forename,surname)
        elif option == 2:
            
        elif option == 3:
            
        elif option == 4:
            
        elif option == 5:
            
        elif option == 6:
            
        elif option == 7:
            
        elif option == 8:
            
        elif option == 9:
            
        elif option == 10:
            
        elif option == 11:
            
main()
