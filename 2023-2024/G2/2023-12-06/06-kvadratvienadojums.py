import math

def kvadratvienadojums(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print(x2, x2)
    elif d == 0:
        x = -b/(2*a)
        print(x)
    else:
        print("sakņu nav")



a = 2
b = 4
c = 3
kvadratvienadojums(a, b, c)