class Calc_Util():
    def check_if_int(res):
        if res % 1 == 0: res = int(res)
            
        return res 
    
    def check_if_letters(num1, num2):
        if not num1.isdigit() or not num2.isdigit():
            print('Can\'t have letters in numbers')
            return False
        else: return True
    
    def check_quit(string):
        # use lower or dictionary here
        if 'Quit' in string or 'Exit' in string:
            exit()

    def remove_spaces(string):
        return string.replace(" ", "")
