try:

    a = int(input("Enter first number: "))

    b = int(input("Enter second number: "))

    print("Select operation :\npress + for addition\npress - for substraction\npress * for multiplication\npress / for division ")

    o = input("Enter operation: ")

    match o:
        case "+":
            print(f"Addition of {a} and {b} is {a+b}")
        case "-":
            print(f"Subtraction of {a} and {b} is {a-b}")
        case "*":
            print(f"Multiplication of {a} and {b} is {a*b}")
        case "/":
            print(f"Division of {a} and {b} is {a/b}")
        case _:
            print("There was an error")

except Exception as e:
    print("Enter a valid value of a and b")