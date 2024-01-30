"""
단어 > 뜻
사물함 100번 키 > 100번 사물함
다른 사람이 100번 키를 더 받을 순 없음
"""
cabinet={3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#print(cabinet[5]) #키에 대한 밸류값이 없으면 에러가 뜨면서 뒤에 코드는 안 뜸
print(cabinet.get(5)) # 키에 대한 밸류값이 없더라도 코드가 정상 출력
print(cabinet.get(7,"사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet={"A-3":"유재석","B-100":"김태호"}

print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["C-20"] ="조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

#KEY 들만 출력
print(cabinet.keys())

#밸류들만 출력
print(cabinet.values())

#키 밸류 둘 다 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)