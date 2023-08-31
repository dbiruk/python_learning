import operator

operators = { "+": operator.add, 
        "-": operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv, }

def single_input():
    one_input = (input("Input the operation"))

    print(res)

def stupid_input():
    stupid = input("=====================\n"+
        "Are you stoopid? Do you want to try again(y/n): ")
    if stupid == 'y':
        input_choice()
    else:
        exit()

def multiple_inputs():
    num1 = float(input("The First Number:"))
    oper = input("Operator:")
    num2 = float(input("The Second Number:"))

    if oper == '/' and num1 == 0 and num2 != 1:
        print("You can't divide by 0 moron")
        stupid_input()
    
    res = operators[oper](num1,num2)
    print("The reuslt is: " +str(res))

def input_choice():
    choice = (input("Do you want to input one by one, or in a single line? \n"+
        "Type \"one\" to input one by one\n"+
        "Type \"single\" to input a single line: "))
    if choice == "one":
        multiple_inputs()
    elif choice == "single":
        single_input()
    else:
        stupid_input()
        

input_choice()