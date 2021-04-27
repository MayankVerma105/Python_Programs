def max3(n1,n2,n3):
    maxNumber = 0
    if n1 > n2:
        if n2 > n3:
            maxNumber = n1
        else:
            maxNumber = n3
            
    elif n2 > n3:
        maxNumber = n2

    else:
        maxNumber = n3

    return maxNumber

def main():
    n1=int(input('Enter first number : '))
    n2=int(input('Enter second number : '))
    n3=int(input('Enter third number : '))
    maximum = max3(n1,n2,n3)
    print('Maximum Number is : ',maximum)

if __name__ == '__main__':
    main()
