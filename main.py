import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

xfactor = random.randint(1,10)
yfactor = -1
count = 0

while xfactor != yfactor:
    count= count+1
    yfactor = input("what is the number?")
    yfactor = int(yfactor)
    if xfactor == yfactor:
        print("congrats")
    elif xfactor > yfactor:
        print("try again choose bigger number")
    elif xfactor < yfactor:
        print("try again choose smaller number")
print(str(count)+" amount of times tried")
