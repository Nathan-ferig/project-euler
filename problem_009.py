def Special_triplet():
    for a in range(1,1000):
        for b in range(a+1,1000):
            c_square = a**2 + b**2
            c = c_square**.5
            if c.is_integer():
                soma = a + b + int(c)
                if soma == 1000:
                    return(a,b,c,soma)
    return("Special triplet not found!")

a,b,c,soma = Special_triplet()
print(a)
print(b)
print(c)
print(soma)
print('Produto de a*b*c: ', a*b*c)