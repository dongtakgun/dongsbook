# score_file = open("score.txt","w", encoding="utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# score_file = open("score.txt","w", encoding="utf8")
# score_file.write("수학 : 0, file = score_file")


#추가 하기 A
# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close



# score_file = open("score.txt","a",encoding="utf8")
# print("도덕 : 80", file = score_file )


#읽어내기
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close

#한줄 읽어내기
score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(),end= " ") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close



#몇 줄인지 모를 떄
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line :
        break   
    print(line)
score_file.close

lines = score_file.readlines() # list형태로 저장
for line in license :
    print(line, end="")

score_file.close
