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
    for i in range(len(parseable) - 1):
        is_var_or_num = lambda x: x.isNumber or len(x) == 1
        if is_var_or_num(parseable[i]) and is_var_or_num(parseable[i + 1]):
            parseable.insert(i + 1, "*")
    return parseable


def format_trig(parseable):
    for i in range(len(parseable)):
        if parseable[i] in trig_list:
            span = first_parantheses(parseable, i)
            input_ = parseable[i+2:span]
            if parseable[i] == trig_list[0]:
                template = ["sin", "(", ")", "/", "cos", "(", ")"]
                adjusted_once = insert_list(template, input_, 2)
                adjusted_twice = insert_list(adjusted_once, input_, len(adjusted_once)-1)
                del parseable[i:span+1]
                insert_list(parseable, adjusted_twice,i + 1)

def insert_list(parseable, insertable, i):
    for j in range(len(insertable)):
        parseable.insert(i,insertable[j])
        i += 1
    return parseable

def first_parantheses(parseable, i):
    char = parseable[i]
    while char != ")":
        i++
        char = parseable[i]
    return i
