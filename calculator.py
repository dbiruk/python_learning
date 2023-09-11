import operator
import calc_util

operators = { "+": operator.add, 
        "-": operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv, }

def calculate (num1, num2, oper):
    res = calc_util.check_if_int(operators[oper](float(num1),float(num2)))
    print("The reuslt is: " + str(res))

def quality_checks(num1, num2, oper):
    if calc_util.check_if_letters(num1, num2) == False or oper not in operators: 
        print("Please learn how to input")
        return False
    if oper == '/' and float(num2) == 0:
        print("You can't divide by 0 moron")
        return False

def single_input():
    one_input = (input("Input the operation: "))
    for x in operators:
        if x in one_input:
            raw_vals = one_input.split(x)
            vals = [s.strip() for s in raw_vals]
            vals.append(x)

    return vals

def multiple_inputs():
    num1 = input("The First Number:")
    oper = input("Operator:")
    num2 = input("The Second Number:")
    vals = [num1, num2, oper]

    return vals

def stupid_input():
    maybe_stupid = input("=====================\n"+
        "Are you stoopid? Do you want to try again(y/n): ")
    if maybe_stupid == 'y':
        return input_choice()
    elif maybe_stupid =='n':
        exit()
    else:
        stupid_input()

def input_choice():
    choice = (input("Do you want to input one by one, or in a single line? \n"+
        "Type \"one\" to input one by one\n"+
        "Type \"single\" to input a single line: "))
    if choice == "one":
        return multiple_inputs()
    elif choice == "single":
        return single_input()
    else:
        stupid_input()


def main():
    vals = input_choice()
    while quality_checks(vals[0], vals[1], vals[2]) == False:
        vals = stupid_input()
    calculate(vals[0], vals[1], vals[2])
    

if __name__ == '__main__':
    main()