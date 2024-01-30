# for waiting_num in [0,1,2,3,4] :
#     print("대기 번호는 {}번 입니다.".format(waiting_num)) 

for waiting_num in range(1,5) : #1에서부터 5미만 까지
    print("대기 번호는 {}번 입니다.".format(waiting_num)) 


starbucks = ["김동현","신영이","블랙보리"]

for 고객 in starbucks :
    print("{} 커피가 준비 되었습니다.".format(고객))


test = ["one","two","three"]
for i in test :         #test 요소를 i에 한 개씩 넣는다.
    print("{}".format(i)) # 포맷으로 {}안에 i를 넣는다
