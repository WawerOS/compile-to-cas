#!/usr/bin/env python3


def insert_list(parseable, insertable, insert_at):
    for j in range(len(insertable)):
        parseable.insert(insert_at, insertable[j])
        insert_at += 1
    return parseable


def first_parantheses(parseable, i):
    char = parseable[i]
    while char != ")":
        i += 1
        char = parseable[i]
    return i
