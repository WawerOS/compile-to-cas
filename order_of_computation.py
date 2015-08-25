#!/usr/bin/env python3
import general_functions

nary_op = ["+", "*"]
binary_op = ["^", "mod", "log"]
unary_op = ["sin", "cos"]


def order_of_computation(orderable):



def order_span(orderable, start_at, end_at):
    recusive_start = general_functions.first_occurence(orderable, start_at, "(")
    if recusive_start < end_at and orderable[recusive_start-1] not in unary_op:
            recusive_end = general_functions.first_occurence(orderable, recusive_start, ")")
            
