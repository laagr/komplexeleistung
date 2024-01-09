import math

def spigot_e(precision):

    # Variabeln
    x = 0
    a = [0,2]
    n = math.ceil(math.log10(math.factorial(precision)))
    while n: 
        a.append(1)
        n = n - 1
    i = a.__len__()
    out = ""
    file1 = open("output-tropf.txt", "w")

    # Loop
    while i > 10:
        n = i 
        i = i - 1
        while n > 1:
            n = n - 1
            a[n] = x % n
            x = 10 * a[n - 1] + x // n
        out = out + str(x)

    file1.write(out)
    file1.close()

spigot_e(10 ** 6)
