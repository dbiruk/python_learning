#xo = ("Montreal", "Tears in the Rain", "After Hours", "Montreal")

# montreal = "Montreal"
# i = 0
# for x in xo:
#     if x == montreal:
#        print(i)
#     i += 1    

# a = [x for(x, montreal) in enumerate(xo) if montreal == "Montreal"]
# print (a)

# xo_dict = {
#     "DawnFM" : {
#         "Intro": "DawnFM",
#         "Last": "Less Than Zero",
#         "Banger": "Sacrifice"
#     },
#     "Starboy" : ["Attention", "Nothing Without You", "Love To Lay"],
#     "After Hours": ["Too Late", "Save Your Tears", "Alone Again"],
#     "Trilogy": [28, "Valerie", "Thursday"],
#     "Kiss Land": ["Professional", "Adaptation", "The Town"]
# }

#print(xo_dict["DawnFM"])

from curses.ascii import isdigit


def check_letters(num1, num2):
    if not num1.isdigit() or not num2.isdigit():
        print('Can\'t have letters in numbers')

check_letters('21', 'ads')