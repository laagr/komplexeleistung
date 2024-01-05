def spigot_e(precision):

    # Variabeln
    x = 0
    a = [0,2]
    n = precision
    while n: 
        a.append(1)
        n = n - 1
    out = ""
    file1 = open("output-tropf.txt", "w")

    # Loop
    while precision > 0:
        n = precision
        precision = precision - 1
        while n > 1:
            n = n - 1
            a[n] = x % n
            x = 10 * a[n - 1] + x // n
        out = out + str(x)

    file1.write(out)
    file1.close()

spigot_e(10 ** 6)
