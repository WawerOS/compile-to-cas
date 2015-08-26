#!/usr/bin/env python3


def insert_list(parseable, insertable, insert_at):
    for j in range(len(insertable)):
        parseable.insert(insert_at, insertable[j])
        insert_at += 1
    return parseable


def first_occurence(parseable, i, findable):
    if i < len(parseable):
        char = parseable[i]
    else:
        return -1
    while char != findable and i < len(parseable):
        i += 1
        if i < len(parseable):
            char = parseable[i]

    if char != findable:
        return -1
    return i
