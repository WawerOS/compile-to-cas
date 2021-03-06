#!/usr/bin/env python3

import sys
import pre_process
import function_parse
import order_of_computation
import var_parse


def main():

    compilable = sys.argv[1]
    preProcessed = pre_process.pre_process(compilable)
    parsed = function_parse.function_parse(preProcessed)
    formatable = order_of_computation.order_span(parsed)
    result = var_parse.var_format(formatable)
    print(result)

if  __name__ == '__main__':
    main()
