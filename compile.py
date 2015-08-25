#!/usr/bin/env python3

import sys
import pre_process
import function_parse
import order_of_computation


def main():
    compilable = sys.argv[1]
    print(compilable)
    preProcessed = pre_process.pre_process(compilable)
    print(preProcessed)
    parsed = function_parse.function_parse(preProcessed)
    print(parsed)
    result = order_of_computation.order_span(parsed, 0, len(parsed)-1)

main()
