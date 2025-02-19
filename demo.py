import random

@staticmethod
def main():
    print(intakeInfo())
    generateRandomNumber()

@staticmethod
def generateRandomNumber():
    x = int(input("Enter the minimum number (X): "))
    y = int(input("Enter the maximum number (Y): "))
    random_number = random.randint(x, y)
    print(f"The random number between {x} and {y} is: {random_number}")

@staticmethod
def intakeInfo():
    age = input("How old are you? ")
    name = input("What is your name? ")
    return "Hello, " + name + "! You are " + age + " years old."

main() # Call the main function