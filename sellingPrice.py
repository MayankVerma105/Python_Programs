def discount(price):
    pass
def sellingPrice(price):
    discountedPrice = discount(price)
    if discountedPrice == None:
        return price
    else:
        return discountedPrice

def main():
    price= int(input('Enter the Price'))
    print('Selling Price is : ',sellingPrice(price))

if __name__ == '__main__':
    main()
