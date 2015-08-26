#!/usr/bin/env python3
import general_functions

nary_op = ["+", "*"]
binary_op = ["^", "mod", "log"]
unary_op = {"sin": "?", "cos": "&"}
unary_op_plus = ["sin", "cos"]
op = ["+", "*", "^", "mod", "log", "sin", "cos"]


def order_span(orderable, start_at, end_at):
    i = start_at + 1
    recusive_end = 0
    recusive_start = 0
    find_end = lambda x: general_functions.first_occurence(orderable, start_at, ")")
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

    l = start_at
    while l < end_at and l < len(orderable):
        if orderable[l] in unary_op_plus:
            replacement = "%s(%s)" % (unary_op[orderable[l]], orderable[l+2])
            print("%s at %s" % (orderable, l))
            del orderable[l:l+3]
            orderable.insert(l, replacement)
            end_at = find_end(1)
            if end_at == -1:
                end_at = 2 ** 32
            # print("%s at %s" % (orderable, l))
        l += 1
        print("l: %s, len(orderable):%s" % (l, end_at))
        print(orderable)

    j = start_at
    while j < end_at and j < len(orderable):
        if orderable[j] == "^":
            leftshift = 1
            rightshift = 1
            if orderable[j-1] == ")":
                leftshift = 2
            if orderable[j+1] == "(":
                rightshift = 2
            replacement = "^(%s,%s)" % (orderable[j-leftshift], orderable[j+rightshift])
            del orderable[j-1:j+2]
            #print("%s at %s" % (replacement, j))
            orderable.insert(j-1, replacement)
            end_at = find_end(1)
            if end_at == -1:
                end_at = 2 ** 32
        j += 1

    k = start_at
    while k < end_at and k < len(orderable):
        if orderable[k] == "mod":
            replacement = "%(%s,%s)" % (orderable[k-1], orderable[k+1])
            del orderable[k-1:k+2]
            orderable.insert(k-1, replacement)
            end_at = find_end(1)
            if end_at == -1:
                end_at = 2 ** 32
            #print("%s at %s" % (orderable, k))
        k += 1

    g = start_at
    while g < end_at and g < len(orderable):
        if orderable[g] == "log":
            replacement = "_(%s,%s)" % (orderable[g-1], orderable[g+1])
            del orderable[g-1:g+2]
            orderable.insert(g-1, replacement)
            end_at = find_end(1)
            if end_at == -1:
                end_at = 2 ** 32
            #print("%s at %s" % (orderable, l))
        g += 1

    z = start_at
    while z < end_at and z < len(orderable):
        if orderable[z] == "*":
            shift = 2
            replacement = "*(%s" % (orderable[z-1])
            save = z-1
            while orderable[z] == "*":
                replacement += ",%s" % (orderable[z+1])
                z += 2
                if z >= len(orderable):
                    break
            replacement += ")"
            del orderable[save:z]
            orderable.insert(save, replacement)
            end_at = find_end(1)
            if end_at == -1:
                end_at = 2 ** 32
            #print("%s at %s" % (orderable, l))
            z -= 1
        z += 1

    x = start_at
    while x < end_at and x < len(orderable):
        if orderable[x] == "+":
            shift = 2
            replacement = "+(%s" % (orderable[x-1])
            save = x-1
            while orderable[x] == "+":
                replacement += ",%s" % (orderable[x+1])
                x += 2
            replacement += ")"
            del orderable[save:x]
            orderable.insert(save, replacement)
            end_at = find_end(1)
            if end_at == -1:
                end_at = 2 ** 32
            #print("%s at %s" % (orderable, l))
            x -= 1
        x += 1
    end_at = general_functions.first_occurence(orderable, start_at, ")")
    if end_at != -1 and end_at < len(orderable):
        del orderable[end_at]
    return orderable
