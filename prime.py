def prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%2 == 0:
            print('Prime Number')
            break
    else:
        flag = True
        return flag


def main():
    n = int(input('Enter a Number : '))
    result = prime(n)
    if result == True:
        print('Its is a Prime number : ',n)
    else:
        print('Its is not a Prime Number: ',n)
        
if __name__ == '__main__':
    main()
    
