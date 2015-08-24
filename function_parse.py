#!/usr/bin/env python3
dictionary_bi_op = {"mod": "_", "/": "*", "-": "+"}
trig_list = ["tan", "cot", "sec", "csc"]


def function_parse(parseable):
    return 0


def format_inverse_ops(parseable):
    for i in range(len(parseable)):
        if parseable[i] in dictionary_bi_op:
            if parseable[i] == "/":
                parseable[i + 1] = "^(%s,-1)" % (parseable[i + 1])
            elif parseable[i] == "-":
                parseable[i + 1] = "*(%s,-1)" % (parseable[i + 1])
            parseable[i] = dictionary_bi_op[parseable[i]]
    return parseable

def format_multiplication(parseable):
    for i in range(len(parseable))-1:
        is_var_or_num = lambda x: x.isNumber or len(x) == 1
        if is_var_or_num(parseable[i]) and is_var_or_num(parseable[i + 1]):
            parseable.insert(i + 1, "*")
    return parseable


def format_trig(parseable):
