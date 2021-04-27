import sys
def main():
    price = input('Enter price of item purchased : ')
    weight = input('Enter weight of item purchased : ')
    try:
        if price == '': price = None
        price = float(price)
        if weight == '': weight = None
        weight = float(weight)
        assert price >= 0 and weight >= 0
        result = price / weight
    except(ValueError, TypeError, ZeroDivisionError):
        print('Invalid input provided by the user \n' + \ str(sys.exc_info())

    else:
        print('Price per unit weight : ', result)

if __name__ == '__main__':
    main()
        
