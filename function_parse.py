#!/usr/bin/env python3
dictionary_bi_op = {"mod": "_", "/": "*", "-": "+"}
trig_list = ["tan", "cot", ]


def function_parse(parseable):
    for i in range(len(parseable)):
        if parseable[i] in dictionary_bi_op:
            if parseable[i] == "/":
                parseable[i + 1] = "^(%s,-1)"%(parseable[i + 1])
            elif parseable[i] == "-":
                parseable [i + 1] = "*(%s,-1)"%(parseable[i + 1])
            parseable[i] = dictionary_bi_op[parseable[i]]
