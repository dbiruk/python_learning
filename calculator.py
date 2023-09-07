import operator
import calc_util

operators = { "+": operator.add, 
        "-": operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv, }

def calculate (num1, num2, oper):
    cil = calc_util.check_if_letters(num1, num2) 
    if cil == False: stupid_input()
    if oper == '/' and float(num2) == 0:
        print("You can't divide by 0 moron")
        stupid_input()   
    
    res = calc_util.check_if_int(operators[oper](float(num1),float(num2)))
    print("The reuslt is: " + str(res))

def single_input():
    one_input = (input("Input the operation: "))
    for x in operators:
        if x in one_input:
            vals = one_input.split(x)
            strip_vals = [s.strip() for s in vals]
            strip_vals.append(x)
    calculate(strip_vals[0], strip_vals[1], strip_vals[2])

def multiple_inputs():
    num1 = input("The First Number:")
    oper = input("Operator:")
    num2 = input("The Second Number:")
    calculate(num1, num2, oper)

def stupid_input():
    maybe_stupid = input("=====================\n"+
        "Are you stoopid? Do you want to try again(y/n): ")
    if maybe_stupid == 'y':
        input_choice()
    elif maybe_stupid =='n':
        exit()
    else:
        stupid_input()


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