import operator
import re 

from calc_util import Calc_Util

operators = { "+": operator.add, 
        "-": operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv, }

def calculate (num1, oper, num2):
    res = Calc_Util.check_if_int(operators[oper](float(num1),float(num2)))
    string_result = f"The reuslt is: {res}"
    print(string_result)
    return res

def quality_checks(num1, oper, num2):
    if Calc_Util.check_if_letters(num1, num2) == False or oper not in operators: 
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

def super_single_input(res =''):
    if res != '':
        one_input = (input(f"{res}"))
    else:
        one_input = (input("Input the operation: "))
    Calc_Util.check_quit(one_input)
    splitted = re.split('([-]?\d+\.\d+)|([-]?\d+)|[a-z]+', one_input, flags=re.IGNORECASE)  #working one
    splitted.insert(0, str(res))
    
    #splitted = re.split('([-]?\d+\.\d+)|[a-z]+', one_input, flags=re.IGNORECASE)
    filtered_list = list(filter(lambda item: item is not None, splitted))
    a = 0
    for x in filtered_list:
        filtered_list[a] = Calc_Util.remove_spaces(x)
        a +=1
    while("" in filtered_list):
        filtered_list.remove("")
    return filtered_list

def multiple_inputs():
    num1 = input("The First Number:")
    oper = input("Operator:")
    num2 = input("The Second Number:")
    vals = [num1, oper, num2]

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
        return super_single_input()
    else:
        stupid_input()

def continious_calcuation(vals,res):
    while quality_checks(vals[0], vals[1], vals[2]) == False:
        vals = stupid_input()
    res = calculate(vals[0], vals[1], vals[2])
    return res


def main():
    vals = input_choice()
    res = ' '
    while quality_checks(vals[0], vals[1], vals[2]) == False:
            vals = stupid_input()
    res = calculate(vals[0], vals[1], vals[2])
    while res != '':
        while quality_checks(vals[0], vals[1], vals[2]) == False:
            vals = stupid_input()
        new_input = super_single_input(res)
        res = continious_calcuation(new_input,res)
   
    

if __name__ == '__main__':
    main()