def calculate(num1, num2, operation):
    if operation == 'add':
        print(num1 + num2)
    elif operation == 'sub':
        print(num1 - num2)
    elif operation == 'mult':
        print(num1 * num2)
    elif operation == 'div':
        if num2 == 0:
            print("Error: division by zero")
            return None
        else:
            print(num1 / num2)
    else:
        print("Error: invalid operation")
        return None