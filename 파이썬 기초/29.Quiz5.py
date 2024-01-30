#50명 탑승 기회
#승객별 운행 소요 시간 5~50분
#소요시간 5~15분 사이 승객만 매칭해야됨

from random import *
cnt=0
승객 = range(1,51)
for i in 승객 :
    소요시간 = randint(5,50)
    if 5 <= 소요시간 <= 15 :
        print("[O]{}번째 손님 (소요시간 :{}분)".format(i,소요시간))
        cnt += 1
    else :
        print("[]{}번쨰 손님 (소요시간 {}분)".format(i,소요시간))

print("총 탑승 승객 : {}".format(cnt))



