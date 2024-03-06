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
       return num1+num2
    
    def performOperation(self, num1, num2, operator):
        if operator == "+":
            return num1+num2
        elif operator == "-":
           return num1-num2
        elif operator == "*":
           return num1*num2
        elif operator == "/" and num2 != 0:
           return num1/num2
        elif operator == "/" and num2 == 0:
            print("Error: Unable to divide by zero.")
        else:
            print("Error: Invalid operator.")
            
    def calculate_square(self, num):
       return num*num
    
    def factorial(self, num):
        if num>0:
            result = 1
            for i in range (1, num+1):
                result*=i
            return result
        else:
            print("Error: Factorial only defined for positive integers.")
            
    def countNumbers(self, num1, num2):
        if num1<num2:
            for i in range (num1, num2+1):
                print(i)
        elif num1>num2:
           for i in range (num1, num2-1, -1):
               print(i)
        else:
            print("Error: Unable to count when numbers are equal.")
    
    def findHypotenuse(self, side1, side2):
       return (self.calculate_square(side1)+self.calculate_square(side2))**(1/2)
        
    def findArea(self, side1, side2):
        if type(side1) or type(side2) == str():
           return str(side1)+str(side2)
        else:
           return str(side1)*str(side2)
        
    def computePower(self, base, exponent):
       return base**exponent
    
    def findType(self, argument):
       return type(argument).__name__

def main():
    calculator = BasicMathOperations()
    end = False
    print("Welcome to the Python calculator tool.")
    while end == False:
        print("                                      ")
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
        print("9 - Compute Power of a Base Given an Exponent")
        print("10 - Return Datatype of Input")
        print("11 - Exit Program")
        print("                                      ")
        print("                                      ")
        option = str(input())
        
        if option == "1":
            forename = input("Please enter your name: ")
            surname = input("Please enter your surname: ")
            calculator.greetUser(forename, surname)
            
        elif option == "2":
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            result = calculator.addNumbers(num1, num2)
            print("The result is:",result)
            
        elif option == "3":
            num1 = float(input("Please enter the first number: "))
            operator = str(input("Please enter the operator: "))
            num2 = float(input("Please enter the second number: "))
            result = calculator.performOperation(num1, num2, operator)
            if result != None:
                print("The result is:",result)
                
        elif option == "4":
            num = float(input("Please enter a number: "))
            result = calculator.calculate_square(num)
            print("The result is:",result)
                
        elif option == "5":
            num = int(input("Please input a positive integer: "))
            result = calculator.factorial(num)
            if result != None:
                print("The result is:",result)
                
        elif option == "6":
            num1 = int(input("Please enter the integer you wish to start counting from: "))
            num2 = int(input("Please enter the integer you wish to count to: "))
            print("Result:")
            print(calculator.countNumbers(num1,num2))
        
        elif option == "7":
            side1 = float(input("Please enter the length of the first side of the right triangle: "))
            side2 = float(input("Please enter the length of the second side of the right triangle: "))
            result = calculator.findHypotenuse(side1, side2)
            print("The result is:",result)

        elif option == "8":
            side1 = input("Please enter the length of the first unique side of the rectangle: ")
            side2 = input("Please enter the length of the second unique side of the rectangle: ")
            result = calculator.findArea(side1, side2)
            print("The result is:",result)
            
        elif option == "9":
            base = float(input("Please enter the value of the base: "))
            exponent = float(input("Please enter the exponent of the base: "))
            result = calculator.computePower(base, exponent)
            print("The result is:",result)
            
        elif option == "10":
            argument = input("Please enter what you wish to check the datatype of: ")
            result = calculator.findType(argument)
            print("The data type of",argument,"is "+result+".")
            
        elif option == "11":
            print("Exiting.")
            end = True
            break
        
        else:
            print("Error: Invalid option. Please select again.")
               
main()
