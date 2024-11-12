#!/usr/bin/env python3

x = 7

for left in range(x):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end = " ")
    print()



