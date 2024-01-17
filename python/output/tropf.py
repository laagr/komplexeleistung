def smallest_factn_k_digits(k):
    n = 0
    factorial = 1
    while len(str(factorial)) < k:
        n = n + 1
        factorial = factorial * n
    return n
    

def spigot_e(precision):

    # Variabeln
    x = 10
    a = [0,2]
    n = smallest_factn_k_digits(precision)
    while n: 
        a.append(1)
        n = n - 1
    i = a.__len__()
    out = ""
    file1 = open("output-tropf.txt", "w")

    # Loop
    while i > 0:
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

