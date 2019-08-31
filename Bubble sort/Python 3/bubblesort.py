#!/usr/bin/env python3
#bublesort.py - buble sort algorithm with python3
sequence  = [4, 2, 7, 3, 5]

for outer in range(len(sequence)):
    for i in range(len(sequence) -1):
        if sequence[i] > sequence[i +1]:
            set1, set2 = sequence[i], sequence[i +1]
            sequence[i], sequence[i +1] = set2, set1
    print(sequence[outer], end = ' ')
print('')