#리턴 개념

def case_1(a,b) :
    return a+b

def case_2(a,b) :
    print(a+b)


print(case_1(2,3)) 
#case_1(2,3) 함수로 들어가 case_1(2,3) = 5로 반환됨 따라서 print(5)가 되어 화면에 5가 출력

print()

print(case_2(2,3))
#case_2(2,3) 함수가 호출 되어 print(a+b)가 화면에 출력 되어서 5가 나옴 하지만 파이썬은 내부적으로 함수를 사용할 떄 반환값이 있어야됨 따라서 5가 출력 되고 나서 case_2(2,3)의 반환값이 none이 되어 print(none) 즉 5 none이 화면에 출력 됨


# https://www.codeit.kr/community/questions/UXVlc3Rpb246NWUzNDUyMjU4MGU1MTMzNzNkOTYzMDIx


print("프린트 없이 함수 사용")

case_1(2,3) # case_1 함수를 호출하지만 case_1(2,3)을 5로 반환하지만 출력하지 않음
print()
case_2(2,3) # case_2 함수를 호출하여 case_2(2,3)을 5로 출력 반환값은 none이지만 반환값을 출력하지 않으므로 none이 나오지 않음

# https://www.codeit.kr/community/questions/UXVlc3Rpb246NWUzNDUyMjU4MGU1MTMzNzNkOTYyZmI1
