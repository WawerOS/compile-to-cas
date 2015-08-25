#!/usr/bin/env python3


def insert_list(parseable, insertable, insert_at):
    for j in range(len(insertable)):
        parseable.insert(insert_at, insertable[j])
        insert_at += 1
    return parseable


def first_occurence(parseable, i, findable):
    char = parseable[i]
    while char != findable and i <= len(parseable):
        i += 1
        char = parseable[i]
    if char != findable:
        return -1
    return i
