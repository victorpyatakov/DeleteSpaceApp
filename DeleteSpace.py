# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:14:18 2020

@author: VPyatakov
"""

# There is delete all unnecassary key space in the line string
def DeleteSpaceInString(string):
    listStr = string.split(" ")
    newStr = ''
    for el in listStr:
        if el != '':
            newStr += el + " "
    return newStr.strip()

def main():
    stringWithoutKeySpace = DeleteSpaceInString(" Привет    Андрей, обними   меня    скорей                     !")
    print(stringWithoutKeySpace)
    
if __name__ == "__main__":
    main()