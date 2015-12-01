#!/usr/bin/env python3
import general_functions

nary_op = ["+", "*"]
binary_op = ["^", "mod", "log", "="]
unary_op = {"sin": "~", "cos": "&"}
unary_op_plus = ["sin", "cos"]
op = ["+", "*", "^", "mod", "log", "sin", "cos"]
find_end = lambda orderable, start_at: general_functions.first_occurence(orderable, start_at, ")")

def order_span(orderable):

    for i in range(len(orderable)):
        recursive_start = general_functions.first_occurence(orderable, i, "(")

        if recursive_start == -1:
            break
        else:

            recursive_end = general_functions.first_occurence(orderable,
                                                             recursive_start,
                                                             ")")
            recursor = orderable[recursive_start+1:recursive_end]
            recursed =  order_span(recursor)
            del orderable  [recursive_start:recursive_end+1]
            orderable = general_functions.insert_list(orderable,recursor,recursive_start)

    orderable = kill_parentheses(orderable)

    orderable = unary_op_template(orderable)

    orderable = binary_op_template(orderable, "^", "^")


    orderable = binary_op_template(orderable, "mod", "%")


    orderable = binary_op_template(orderable, "log", "_")


    orderable = nary_op_template(orderable, "*")


    orderable = nary_op_template(orderable, "+")

    end_at = general_functions.first_occurence(orderable, 0, ")")
    if end_at != -1 and end_at == len(orderable) - 1:
        del orderable[end_at]
    return orderable


def unary_op_template(orderable):
    for l  in range(len(orderable)):
        if l >= len(orderable):
            break
        elif orderable[l] in unary_op_plus:
            replacement = "%s(%s)" % (unary_op[orderable[l]], orderable[l+1])
            del orderable[l:l+2]

            orderable.insert(l, replacement)
    return orderable


def binary_op_template(orderable, op, symbol):
    for j in range(len(orderable)):
        if orderable[j] == op:
            leftshift = 1
            rightshift = 1
            if orderable[j-1] == ")":
                leftshift = 2
            if orderable[j+1] == "(":
                rightshift = 2
            replacement = "(%s,%s)" % (orderable[j-leftshift], orderable[j+rightshift])
            replacement = symbol + replacement
            del orderable[j-1:j+2]
            orderable.insert(j-1, replacement)

    return orderable


def nary_op_template(orderable, op):
    z = 0
    while z < len(orderable):
        if orderable[z] == op:
            shift = 2
            replacement = "(%s" % (orderable[z-1])
            save = z-1
            while orderable[z] == op:
                replacement += ",%s" % (orderable[z+1])
                z += 2
                if z >= len(orderable):
                    break
            replacement += ")"
            replacement = op + replacement
            del orderable[save:z]
            orderable.insert(save, replacement)

            z -= 1
        z += 1
    return orderable


def kill_parentheses(orderable):
    for i in range(len(orderable)):
        current_val = i
        if orderable[current_val] in ["(", ")"]:
                del orderable[current_val]
    return orderable
