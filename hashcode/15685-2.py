a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
global gcd1
global gcd2


def gcd1(a, b):
  while a%b != 0:
    temp = a%b
    a = b
    b = temp
    global gcd1
    gcd1 = b

def gcd2(gcd1, c):
  while gcd1%c != 0:
    temp = gcd1%c
    gcd1 = c
    c = temp
    global gcd2
    gcd2 = c 


lcm1 = (a * b) / gcd2
lcm2 = (lcm1 * c) / gcd2
print(gcd2, "%g" %(lcm2))









