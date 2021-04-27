def printTable(num, nMultiples = 10):
    for multiple in range(1, nMultiples + 1):
        product = num * multiple
        print(num,'*','%2d'% multiple, '=' , '%5d'% product)

def main():
    num = int(input('Enter the Number : '))
    printTable(num)

if __name__ == '__main__':
    main()
