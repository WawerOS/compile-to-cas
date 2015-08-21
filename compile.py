#!/usr/bin/env python3

import sys
import pre_process


def main():
    compilable = sys.argv[1]
    print(compilable)
    preProcessed = pre_process.pre_process(compilable)
    print(preProcessed)

if __name__ == '__main__':
    main()
