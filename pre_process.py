#!/usr/bin/env python3

operators = ["+", "-", "/", "*", "^", "mod", "log", "sin", "cos", "cot", "tan", "sec", "csc"]
numbers = ["1", "2", "3", "4", "5", "6", "8", "9", "0", "."]


# Takes standard mathematical expressions
# and returns a list of terms and operators
def pre_process(compilable):
    preProcessed = []
    not_done = True
    count = 0

    while not_done:
        one_character = compilable[count]
        three_characters = compilable[count:(count+3)]

        if checkIfOperator(one_character):
            preProcessed.append(one_character)

        elif checkIfOperator(three_characters):
            preProcessed.append(three_characters)
            count += 2

        elif checkIfNumber(one_character):
            shift = 1
            not_done_two = True
            while not_done_two:
                if count+shift >= len(compilable):
                    break
                num = compilable[count+shift]
                not_done_two = checkIfNumber(num)
                if not_done_two:
                    shift += 1
            preProcessed.append(compilable[count:(count+shift)])
            count += (shift - 1)

        else:
            if not(one_character == " "):
                preProcessed.append(one_character)

        count += 1
        if count >= len(compilable):
            not_done = False
    return preProcessed


# Checks if a string is a operator
def checkIfOperator(input):
    isOp = False
    for op in operators:
        isOp = op == input
        if isOp:
            break

    return isOp


# Checks if a string is a part of the numbers list
def checkIfNumber(input):
    isNumber = False
    for num in numbers:
        isNumber = num == input
        if isNumber:
            break
    return isNumber
