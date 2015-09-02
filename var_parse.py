#!/usr/bin/env python3
import string
restricted_chars = ["+", "*", "^", "%", "_", "~", "&", "=", "(", ",", ")"]


def var_format(formatable):
    vars = []
    formatable = formatable[0]
    for char in formatable:
        if not(char in restricted_chars) and not(char in string.digits):
            vars.insert(0, char)
    vars = set(vars)
    vars = list(vars)
    formatable_2 = ":" + formatable
    for var in vars:
        formatable_2 = var + formatable_2
    return formatable_2
