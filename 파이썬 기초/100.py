def std_weight(키,성별):
    if 성별 == "남자" :
        return 키*키*22
    else :
        return 키*키*21

키 = input("키를 입력해주세요")
성별 = input("성별을 입력해주세요")
키 = int(키)
weight = round(std_weight(키/100,성별),2)

print("키 {}cm {}의 표준 체중은 {}입니다.".format(키,성별,weight))

