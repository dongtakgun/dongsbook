#출석 번호 1,2,3,4 앞에 100을 붙이기로 함 > 101 102 103 104
# student = [1,2,3,4,5]
# student = [i + 100 for i in student]
# print(student)

#학생 이름을 길이로 변환

# student = ["아이언맨","토르","그루트"]

# student = [len(i) for i in student]

# print(student)

#학생 이름을 대문자로 변환

student = ["iron man","thor","groot"]
student = [i.upper() for i in student]

print(student)