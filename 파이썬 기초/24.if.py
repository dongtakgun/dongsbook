# wheather = input("오늘 날씨는 어떄요?")

# if wheather == "비" or wheather == "눈" :
#     print("우산을 챙기세요")
# elif wheather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")    


temp = int(input("오늘 날씨 어떄요?"))
if temp >=30 :
    print("너무 더워요 나가지 마세요")
elif temp >=10 and temp <= 30 :
    print("날씨 좋아요")
elif 0<= temp <=10 :
    print("외투 가져가")
else :
    print("개 춥다 나가지 마라")