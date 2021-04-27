def mySine(x):
    epsilon = 0.00001
    multBy = -x**2
    term = x
    total = x
    nxtInSeq = 2.0
    while abs(term) > epsilon:
        divBy = nxtInSeq*(nxtInSeq + 1)
        term = term * multBy / divBy
        total += term
        nxtInSeq += 2
    return total
