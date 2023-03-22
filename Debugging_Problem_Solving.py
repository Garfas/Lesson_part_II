# 2023_03_21
#Jam priklauso failas .env
import sys

total = 0

for arg in sys.argv[1:]:
    try:
        num = float(arg)
        total += num

    except ValueError:
        print("Error: invalid argument '{}'".format(arg))
        sys.exit(1)

print("Total: {}".format(total))