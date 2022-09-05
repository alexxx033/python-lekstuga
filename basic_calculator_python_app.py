# define the function needed, add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# add a while loop to continue until the user exit

from __future__ import print_function


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")


def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. EXIT \n")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program Ended")
        quit()
    else:
        print("Wrong Input, Try again")