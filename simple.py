a = 0
b = 1
temp = 0
s = 0

def fib():
    global a
    global b
    global s
    global temp
    if b % 2 == 0:
        s += b
        print(b)
    temp = a + b
    a = b
    b = temp

    if b < 4000000:
        fib()

fib()
print(s)