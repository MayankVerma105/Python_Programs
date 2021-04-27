'''
def triangle(n,nRows):
    k = n- 1
    nSpaces = 0
    nStars = 2 * nRows - 1
    for i in range(0,n):
        print(' '* nSpaces + '*' * nStars)
        nStars -= 2
        nSpaces += 1
        for j in range(0,k):
            print(end =' ')
        k = k- 1
        for j in range(0, i+ 1):
            print('* ',end='')
        print('\r')
    
        
#driver Code
nRows = 10
n = 5
triangle(n,nRows)
'''
'''
def numpat(n):
    num = 1
    for i in range(0,n):
        num = 1
        for j in range(0, i+1):
            print(num, end= ' ')
            num = num + 1
        print('\r')

#Driver Class
n = 5
numpat(n)
'''
'''
def pypart(n):
    k = 2*n- 2
    for i in range(0, n):
        for j in range(0,k):
            print(end=' ')
        k = k - 2
        for j in range(0,i+1):
            print('* ', end='')
        print('\r')

#Driver class
n = 5
pypart(n)
'''
