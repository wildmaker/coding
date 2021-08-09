# 按固定宽度打印价格列表（小票）

WIDTH  = 35

while True:
    printing = ""
    price_tags = {}
    while printing!='print':
        item = input("Please enter the item's name:")
        price = input("Please enter the item's price:")
        print("item:"+ item + "\n" + "price:"+ price)
        price_tags[item] = price
        printing = input("Please enter 'print' to print.")

    print("This is your list:")
    print('=' * WIDTH)
    print("Item%*s" % (WIDTH-4,"price"))
    print('-' * WIDTH)
    for key, value in price_tags.items():
        print("%s%*.*f" % (key,WIDTH-len(key),2,float(value)))
    print('=' * WIDTH)