#!/usr/bin/env python3
import general_functions

nary_op = ["+", "*"]
binary_op = ["^", "mod", "log"]
unary_op = {"sin": "?", "cos": "&"}
op = ["+", "*", "^", "mod", "log", "sin", "cos"]


def order_span(orderable, start_at, end_at):
    i = start_at
    recusive_end = 0
    recusive_start = 0
    while i < end_at and i != -100:
        recusive_start = general_functions.first_occurence(orderable, i, "(")
        if recusive_start < end_at:
            recusive_end = general_functions.first_occurence(orderable,
                                                             recusive_start,
                                                             ")")
            replacement = order_span(orderable, recusive_start, recusive_end)
            del orderable[recusive_start:recusive_end+1]
            orderable.insert(recusive_start, replacement)
        i += 1

    j = start_at
    while j < end_at:
        if orderable[j] == "^":
            replacement = "^(%s,%s)" % (orderable[j-1], orderable[j+1])
            del orderable[j-1:j+2]
            orderable.insert(j-1, replacement)
        j += 1

    k = start_at
    while k < end_at:
        if orderable[k] == "mod":
            replacement = "%(%s,%s)" % (orderable[k-1], orderable[k+1])
            del orderable[k-1:k+2]
            orderable.insert(k-1, replacement)
        k += 1

    g = start_at
    while g < end_at:
        if orderable[g] == "log":
            replacement = "_(%s,%s)" % (orderable[g-1], orderable[g+1])
            del orderable[g-1:g+2]
            orderable.insert(g-1, replacement)
        g += 1

    l = start_at
    while l < end_at:
        if orderable[l] in unary_op.keys():
            replacement = "%s(%s)" % (unary_op[l], orderable[l+1])
            del orderable[g:g+2]
            orderable.insert(g, replacement)
        l += 1

    z = start_at
    while z < end_at:
        if orderable[z] == "*":
            shift = 2
            replacement = "*(%s" % (orderable[z-1])
            save = z-1
            while orderable[z] == "*":
                replacement += ",%s" % (orderable[z+1])
                z += 2
            replacement += ")"
            del orderable[save:z]
            orderable.insert(save, replacement)
            z -= 1
        z += 1

    x = start_at
    while x < end_at:
        if orderable[x] == "*":
            shift = 2
            replacement = "*(%s" % (orderable[x-1])
            save = x-1
            while orderable[x] == "*":
                replacement += ",%s" % (orderable[x+1])
                x += 2
            replacement += ")"
            del orderable[save:x]
            orderable.insert(save, replacement)
            x -= 1
        x += 1

    return orderable[start_at]
