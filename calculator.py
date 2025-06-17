def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={'+':add, '-':subtract, '*':multiply, '/':divide}
def calculator():
    should_accumulate = True
    num1=float(input("Enter your first number: "))
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol= input("Enter your operation symbol: ")
        num2=float(input("Enter your second number: "))
        answer=operations[operation_symbol](num1,num2)
        print(f"answer is {num1}{operation_symbol}{num2}={answer}")
        choice=input(f"Do you want to continue calculation with {answer}? Type 'yes' or 'no': ").lower()
        if choice=="yes":
            num1=answer

        else:
            should_accumulate = False
            print("/n"*20)
            calculator()
calculator()
