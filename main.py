import vending_machine.vending_service as machine

flag = True  # 控制迴圈是否繼續執行

while flag:
    print('\n============================')
    select = eval(input('1. 儲值\n2. 購買\n3. 查詢餘額\n4. 離開\n請選擇：'))

    if select == 1:  # 儲值
        machine.deposit()

    elif select == 2:  # 購買
        machine.buy()

    elif select == 3:  # 查詢餘額
        print(f'目前餘額為 {machine.balance}元')

    elif select == 4:  # 離開
        print('bye')
        flag = False  # 將flag改為False就會跳出迴圈
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue


print('hello git')