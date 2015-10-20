#!/usr/bin/env python3
# TODO Reformat into one loop with three options
import general_functions

dictionary_bi_op = {"mod": "_", "/": "*", "-": "+"}
trig_list = ["tan", "cot", "sec", "csc"]


def function_parse(parseable):
    parsed_once = format_multiplication(parseable)
    parsed_twice = format_inverse(parseable)
    parsed_thrice = format_trig(parsed_once)
    return parsed_thrice


# Changes all division into multiplication and subtraction into addtion.
# Depends heavily on the format_inverse_template function.
def format_inverse(parseable):

    for i in range(len(parseable)):
        if parseable[i] == "/":
            insertable = ["^", "-1"]
            parseable = format_inverse_template(parseable, insertable, i)
            parseable[i] = "*"

        elif parseable[i] == "-":
            insertable = ["*", "-1"]
            parseable = format_inverse_template(parseable, insertable, i)
            parseable[i] = "+"

    return parseable


# Changes all side by side non-numerical values into
# multiplied versions of these values
def format_multiplication(parseable):
    for i in range(len(parseable)-1):
        is_not_bi_op = lambda x: x not in ["*", "+", "/", "-", "mod", "log"]
        if is_not_bi_op(parseable[i]) and is_not_bi_op(parseable[i+1]):
            if parseable[i] != "(" and parseable[i+1] != ")":
                if parseable[i] not in trig_list and parseable[i + 1] != "(":
                    if parseable[i] not in ["sin", "cos"] and parseable[i + 1] != "(":
                        parseable.insert(i + 1, "*")
    return parseable


# Changes all trigonometric functions into statements with sine and cosine
# Depends heavily on the format_trig_tmeplate
def format_trig(parseable):
    i = 0
    for i in range(len(parseable)):
        if parseable[i] in trig_list:
            span = general_functions.first_occurence(parseable, i, ")")
            input_ = parseable[i+2:span]
            tan_or_sec = lambda x: x == "tan" or x == "cot"
            templates = {"tan": ["sin", "(", ")", "*", "cos", "(", ")", "^", "-1"],
                         "cot": ["cos", "(", ")", "*", "sin", "(", ")", "^", "-1"],
                         "sec": ["cos", "(", ")", "^", "-1"],
                         "csc": ["sin", "(", ")", "^", "-1"]}
            adjusted = format_trig_tmeplate(templates[parseable[i]], input_, tan_or_sec(parseable[i]))

            del parseable[i:span+1]
            general_functions.insert_list(parseable, adjusted, i)
            
    return parseable


# Used to allow more reusable code
def format_inverse_template(parseable, insertable, i):
    if parseable[i+1] in trig_list or parseable[i] in ["sin", "cos", "("]:
        insert_at = general_functions.first_occurence(parseable, i, ")") + 1
    else:
        insert_at = i + 2
    parseable = general_functions.insert_list(parseable, insertable, insert_at)
    return parseable


# Used to allow more reusable code
def format_trig_tmeplate(template, input_, tan_or_sec):
    offset_one = 2
    adjusted_once = general_functions.insert_list(template, input_, offset_one)

    if tan_or_sec:
        adjusted_twice = general_functions.insert_list(adjusted_once, input_,
                                                       len(adjusted_once)-3)
        return adjusted_twice
    else:
        return adjusted_once
