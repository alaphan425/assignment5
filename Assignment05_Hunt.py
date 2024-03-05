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
        
        