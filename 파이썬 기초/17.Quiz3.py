# http://naver.com
# http://부분 제외
# .이후 부분 제외
# 처음 세자리 글자 갯수 글자 내 e 갯수 !구성

Url= "http://naver.com"

U= Url.replace("http://","")[:5]

PW=Url.replace("http://","")[:3] + str(len(U)) + str(Url.count("e")) + "!"

print(PW)
