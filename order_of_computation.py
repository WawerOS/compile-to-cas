#!/usr/bin/env python3
import general_functions

nary_op = ["+", "*"]
binary_op = ["^", "mod", "log", "="]
unary_op = {"sin": "~", "cos": "&"}
unary_op_plus = ["sin", "cos"]
op = ["+", "*", "^", "mod", "log", "sin", "cos"]
find_end = lambda orderable, start_at: general_functions.first_occurence(orderable, start_at, ")")

def order_span(orderable, start_at, end_at):
    i = start_at + 1
    recusive_end = 0
    recusive_start = 0
    while i < end_at:
        recusive_start = general_functions.first_occurence(orderable, i, "(")
        #print(recusive_start)

        if recusive_start == -1:
            break
        elif recusive_start < end_at:
            recusive_end = general_functions.first_occurence(orderable,
                                                             recusive_start,
                                                             ")")
            orderable = order_span(orderable, recusive_start, recusive_end)
            #print(orderable)

        i += 1

    orderable = kill_parentheses(orderable, start_at, end_at)

    orderable_tuple = unary_op_template(orderable, start_at, end_at)
    orderable = orderable_tuple[0]
    end_at = orderable_tuple[1]

    orderable_tuple = binary_op_template(orderable, start_at, end_at, "^", "^")
    orderable = orderable_tuple[0]
    end_at = orderable_tuple[1]

    orderable_tuple = binary_op_template(orderable, start_at, end_at, "mod", "%")
    orderable = orderable_tuple[0]
    end_at = orderable_tuple[1]

    orderable_tuple = binary_op_template(orderable, start_at, end_at, "log", "_")
    orderable = orderable_tuple[0]
    end_at = orderable_tuple[1]

    orderable_tuple = nary_op_template(orderable, start_at, end_at, "*")
    orderable = orderable_tuple[0]
    end_at = orderable_tuple[1]

    orderable_tuple = nary_op_template(orderable, start_at, end_at, "+")
    orderable = orderable_tuple[0]
    end_at = orderable_tuple[1]

    end_at = general_functions.first_occurence(orderable, start_at, ")")
    if end_at != -1 and end_at == len(orderable) - 1:
        del orderable[end_at]
    return orderable


def unary_op_template(orderable, start_at, end_at):
    l = start_at
    while l < end_at and l < len(orderable):
        if orderable[l] in unary_op_plus:
            replacement = "%s(%s)" % (unary_op[orderable[l]], orderable[l+1])
            print("%s at %s" % (orderable, l))
            del orderable[l:l+2]
            orderable.insert(l, replacement)
            end_at = find_end(orderable, start_at)
            if end_at == -1:
                end_at = 2 ** 32
        l += 1
    return (orderable, end_at)


def binary_op_template(orderable, start_at, end_at, op, symbol):
    j = start_at

    while j < end_at and j < len(orderable):
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
            end_at = find_end(orderable, start_at)
            if end_at == -1:
                end_at = 2 ** 32
        j += 1

    return (orderable, end_at)


def nary_op_template(orderable, start_at, end_at, op):
    z = start_at
    while z < end_at and z < len(orderable):
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
            end_at = find_end(orderable, start_at)
            if end_at == -1:
                end_at = 2 ** 32
            z -= 1
        z += 1
    return (orderable, end_at)


def kill_parentheses(orderable, start_at, end_at):
    for i in range(end_at - start_at):
        current_val = i + start_at
        if current_val > start_at and current_val < end_at and current_val < len(orderable):
            if orderable[current_val] in ["(", ")"]:
                del orderable[current_val]
    return orderable
