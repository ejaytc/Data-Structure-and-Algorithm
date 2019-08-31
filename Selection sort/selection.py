#!/usr/bin/env python3
#Insertion algorithm
sequence  = [4, 2, 7, 3, 5]
imin = 0

for iouter in range(len(sequence) -2):
    imin = iouter
    for iinner in range(iouter +1, len(sequence) -1):
        if sequence[iinner] < sequence[imin]:
            imin = iinner
    sequence[imin], sequence[iouter] = sequence[iouter], sequence[imin]

for display in sequence:
    print(display, end = ' ')
print()
