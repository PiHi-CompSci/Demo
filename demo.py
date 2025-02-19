

@staticmethod
def main():
    intakeInfo()

@staticmethod
def intakeInfo():
    age = input("How old are you? ")
    name = input("What is your name? ")
    return "Hello, " + name + "! You are " + age + " years old."

main() # Call the main function