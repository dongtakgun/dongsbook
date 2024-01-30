print("python","java")
print("python"+"java")
print("python","java",sep=",")
print("python","java",sep=" vs ")
print("python","java","javascript", sep=" vs ")
print("python","java",sep=",",end="?")
print("무엇이 더 재밌을까요?")

#sep= "" ,자리에 넣는 것을 정할 수 있음
#end = "?" 마지막에 ?를 넣으면서 줄바꿈 생략


# import sys
# print("python","java",file=sys.stdout) #표준 출력
# print("python","java",file=sys.stderr) #표준 에러

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject,score in scores.items():
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":")

#은행 대기순번표
#001,002,003,...

for num in range(1,21):
    print("대기번호 :" +str(num).zfill(3))


answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
#print("입력하신 값은" + answer + "입니다.")

#사용자 입력을 통해 값을 받으면 항상 문자열
