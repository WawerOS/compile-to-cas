#!/usr/bin/env python3

import sys
import pre_process
import function_parse


def main():
    compilable = sys.argv[1]
    print(compilable)
    preProcessed = pre_process.pre_process(compilable)
    print(preProcessed)
    parsed = function_parse.function_parse(preProcessed)
    print(parsed)

if __name__ == '__main__':
    main()
