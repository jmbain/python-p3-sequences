#!/usr/bin/env python3

def print_fibonacci(length):
    result = []
    if length == 0:
        print(result)
    elif length == 1:
        result.append(0)
        print(result)
    elif length == 2:
        result =[0, 1]
        print(result)
    elif length > 2:
        result = [0, 1]
        for i in range(2, length):
            result.append(result[-1] + result[-2])
        print(result)