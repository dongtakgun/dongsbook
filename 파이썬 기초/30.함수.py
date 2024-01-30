def open_account():
    print("새로운 계좌가 개설되었습니다.")

def deposit(잔액,입금액):
    print("입금이 완료되었습니다. 잔액은{}원 입니다.".format(잔액 + 입금액))
    return 잔액 + 입금액    


"""
def withraw(잔액,출금액):
    if 잔액 >= 출금액 :
        print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(잔액 - 출금액))
        return 잔액 - 출금액
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {}원입니다.".format(잔액))
        return 잔액
"""

def withraw_night(잔액,출금액) : #저녁에 출금
    수수료 = 100 #수수료 100원
    if 잔액 >= 출금액 + 수수료 :
        print("출금이 완료되었습니다. 수수료는 {}원 잔액은 {}원입니다.".format(수수료,잔액 - 출금액 - 수수료))
        return 수수료, 잔액 - 수수료 - 출금액
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {}원입니다.".format(잔액))
    return 잔액

open_account()
잔액 = 0

잔액 = deposit(잔액, 1000)
#잔액 = withraw(잔액, 2000)
#잔액 = withraw(잔액, 500)
수수료, 잔액 = withraw_night(잔액 ,500)

