결석 = [2,5]
노책 = [7]
for student in range(1,10) :
    if student in 결석 :
        continue
    elif student in 노책 :
        print("오늘 수업 여기까지 {}는 교무실로 따라와".format(student))
        break
    print("{}야 책 읽어봐.".format(student))