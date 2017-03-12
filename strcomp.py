# encoding declaration
"""coding=utf-8"""
from colorama import Fore, Back, Style


# function definition
def strCompare(str1, str2):
    str1Array = list(str1)
    str1Array = sorted(str1Array)
    str1Array = ''.join(str1Array)

    str2Array = list(str2)
    str2Array = sorted(str2Array)
    str2Array = ''.join(str2Array)

    if len(str1) == len(str2):
        if str1 == str2:
            return 'equal'
        elif str1Array == str2Array:
            return True
        else:
            return False
    else:
        return False


# input loop
while True:
    # script description and user input prompt
    print(Fore.RED + '\n=====================================' + Fore.YELLOW + 'v1.1.170312' + Fore.RESET)
    print(Fore.CYAN + 'This Python script will compare two strings to\ndetermine if both are equal in length, letters,\nand word...' + Style.DIM + Fore.WHITE + '\n(For exit, press Enter in any of the inputs.)' + Fore.RESET + Style.RESET_ALL)
    print(Fore.BLUE + '------------------------------------------------' + Fore.RESET)
    try:
        userStr1 = raw_input(Fore.YELLOW + 'Enter a First String value: ' + Fore.RESET)
        userStr2 = raw_input(Fore.YELLOW + 'Enter a Second String value: ' + Fore.RESET)
    except NameError:
        userStr1 = input(Fore.YELLOW + 'Enter a First String value: ' + Fore.RESET)
        userStr2 = input(Fore.YELLOW + 'Enter a Second String value: ' + Fore.RESET)
    print(Fore.RED + '================================================\n' + Fore.RESET)

    # user inputs evaluation
    if userStr1 == '' or userStr2 == '':
        print(Back.MAGENTA + '-----------------' + Back.RESET)
        print(Back.MAGENTA + '|' + Back.RESET + Style.BRIGHT + '  Good Bye!!!  ' + Style.RESET_ALL + Back.MAGENTA + '|' + Back.RESET)
        print(Back.MAGENTA + '-----------------' + Back.RESET + '\n')
        break
    elif userStr1.isalpha() and userStr2.isalpha():
        # call function
        compareResult = strCompare(userStr1, userStr2)

        # console outputs
        if compareResult == 'equal':
            print(Back.BLUE + Fore.WHITE + ' String(1) and String(2) is the same string. ' + Fore.RESET + Back.RESET + '\n')
            break
        elif compareResult:
            print(Back.GREEN + Fore.WHITE + ' String(1) and String(2) are equal in length and containg the same letters. ' + Fore.RESET + Back.RESET + '\n')
            break
        else:
            print(Back.YELLOW + Fore.RED + ' String(1) and String(2) are different strings. ' + Fore.RESET + Back.RESET + '\n')
            break
    else:
        print(Back.RED + ' *** INPUT ERROR *** ' + Back.RESET + '\n' + Back.RED + ' Input value should be a String. ' + Back.RESET)
        continue
