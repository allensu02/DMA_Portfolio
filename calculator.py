import sys
import math

def pythagor(a,b):
    a2 = math.pow(a,2);
    b2 = math.pow(b,2);
    c = math.sqrt(a2 + b2);
    return c

def circlearea (a):
    area = math.pi * math.pow(a,2);
    return area;


def main ():

    command = sys.argv[1]


    if command == "add":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print (x + y)

    if command == "multiply":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print (x * y)

    if command == "divide":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x/y)

    if command == "subtract":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x - y)

    if command == "countto":
        x = int(sys.argv[2])

        for i in range (x):
            print (i) + 1
    if command == "pythagorean":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(pythagor(x,y))
    if command == "circlearea":
        x = int(sys.argv[2])
        print (circlearea(x))

list = ["asdf", "sdfsdf"]
print(list)
if __name__ == '__main__':
    main()