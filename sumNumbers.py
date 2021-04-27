def main():
    total = 0
    number = input('Enter a Number : ')
    while number != '':
        total += int(number)
        number = input('Enter a Number : ')
    print('Sum of all the numbers is : ',total)

if __name__ == '__main__':
    main()
