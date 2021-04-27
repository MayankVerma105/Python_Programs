import sys
def main():
    price = input('Enter price of the item')
    weight = input('Enter weight of the item')
    try:
        if price == '': price = None
        price = float(price)
        if weight == '': weight = None
        weight = float(weight)
        assert price >= 0 and weight >= 0
        result = price / weight
    except ValueError:
        print('Invalid inputs : ValueError')
    except TypeError:
        print('Invalid inputs : TypeError')
    except ZeroDivisionError:
        print('Invalid inputs : ZeroDivisionError')
    except:
        print(str(sys.exc_info()))
    else:
        print('Price per unit weight',result)

if __name__ == '__main__':
    main()
