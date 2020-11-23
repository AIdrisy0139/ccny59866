'''
Ministat Generator
Group A
'''

import sys
import random


def main():
    fName = str(sys.argv[1])
    length = int(str(sys.argv[2]))
    file = open(fName,"w+")
    for i in range(0, length):
        rndm = random.randint(0,2**32-1)
        print(f"{rndm}", file=file)
    return 0


main()