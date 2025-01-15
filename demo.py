# Description: A simple Python script that does some random stuff as a demo for VCS


@staticmethod
# Define the main function: this is the entry point of the script
def main():
    intakeInfo() # Call the intakeInfo function

@staticmethod
def intakeInfo():
    age = input("What year were you born? ")
    name = input("What do you like to be called? ")
    return "Hello, " + name + "! You are " + age + " years old."

main() # Call the main function