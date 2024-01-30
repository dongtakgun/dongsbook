donghyun = "000524-3184610"

print("성별 :" + donghyun[7])   # 컴퓨터 인덱싱은 1부터가 아니라 0부터

print("연도 :" + donghyun[0:2])     #0부터 2직전까지 즉 (0,1)만
print("월 :" + donghyun[2:4])
print("일 : " + donghyun[4:6])

print("생년월일 :" + donghyun[:6]) #처음부터 6직전까지
print("뒤 7자리 :" + donghyun[7:]) #7부터 끝까찌

print("뒤 7자리" + donghyun[-7:])   #맨 뒤에서부터 -1 -2 -3 -4


