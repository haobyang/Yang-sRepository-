balance = 0  # 使用者餘額

#  品項
drinks = [
    {'name': '可樂', 'price': 20},
    {'name': '雪碧', 'price': 20},
    {'name': '茶裏王', 'price': 25},
    {'name': '原萃', 'price': 25},
    {'name': '純粹喝', 'price': 30},
    {'name': '水', 'price': 20}
]


def deposit():
    """
    儲值功能
    :return: nothing
    """
    global balance  # 告訴函式這裡需要用到「全域變數」balance
    value = eval(input('儲值金額：'))

    #  檢查輸入金額是否大於0，若沒有則要求重新輸入
    while value < 1:
        print('====儲值金額需大於零====')
        value = eval(input('儲值金額：'))

    balance += value  # 目前餘額+輸入金額
    print(f'儲值後金額為 {balance}元')


def buy():
    """
    購買功能
    :return: nothing
    """
    global balance, drinks  # 告訴函式這裡需要用到「全域變數」balance及drinks
    print('請選擇商品')
    for i in range(len(drinks)):
        print(f'{i + 1}. {drinks[i]["name"]}  {drinks[i]["price"]}元')

    choose = eval(input('請選擇編號：'))

    #  檢查輸入選項是否介於1-6之間，若沒有則要求重新輸入
    while choose < 1 or choose > 6:
        print("請輸入1-6之間")
        choose = eval(input("請選擇："))

    buy_drink = drinks[choose - 1]  # 使用者選擇的品項

    #  檢查餘額是否足夠購買商品，若不足則詢問是否需要儲值
    while balance < buy_drink['price']:
        print('====餘額不足，需要儲值嗎？====')
        want_deposit = input('y/n?')
        if want_deposit == 'y':
            deposit()
        elif want_deposit == 'n':
            break
        else:
            print('====請重新輸入====')

    # 儲值後餘額大於商品金額再購買
    if balance >= buy_drink['price']:
        balance -= buy_drink['price']
        print(f'已購買{buy_drink["name"]}  {buy_drink["price"]}元')
        print(f'購買後餘額為 {balance}元')



