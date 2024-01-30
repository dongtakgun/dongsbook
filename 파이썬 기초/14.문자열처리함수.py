python = "Python is Amazing"

print(python)

print(python.lower())
print(python.upper())

print(len(python))
print(python[0].isupper())

print(python.replace("Python","Java"))

index = python.index("n")
print(index)

index = python.index("n", index+1)  #두 번째 n을 찾으려고 할 떄
print(index)

print(python.find("Java"))  #찾고자 하는 게 없으면 -1이 출력값
#print(python.index("java")) #찾고자 하는 게 없으면 에러를 띄우면서 다음 문장을 실행하지 않고 끝냄

print(python.count("n"))


print("hi")
