# def std_weight(키,성별):
#     if 성별 == "남자":
#         print("키 {}m 남자의 표준 체중은 {}입니다.".format(키,str(키*키*22)[:5]))
#     else :
#         print("키 {}m 여자의 표준 체중은 {}입니다.".format(키,str(키*키*21)[:5]))

# std_weight(1.75,"남자")
# std_weight(1.62,"여자")


def std_weight(키,성별):
    if 성별 == "남자" :
        return 키*키*22
    else :
        return 키*키*21

키 = 175
성별 = "남자"
weight = round(std_weight(키/100, 성별),2)


print("키 {}cm {}의 표준 체중은 {}입니다.".format(키,성별,weight))
