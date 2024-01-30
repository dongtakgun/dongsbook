# 집합 (set) 중복이 안 되고 순서가 없음


my_set = {1,2,3,3,3}
print(my_set)


java = {"유재석","김동현","신영이"}
#python = set (["유재석","박명수"])
python = {"김동현","박명수"}


#교집합

print(java & python)
print(java.intersection(python))

#합집함
print(java | python)
print(java.union(python))

#차집합 java는 할 수 있지만 python은 할 줄 모르는 개발자
print(java - python)
print(java.difference(python))

#파이썬을 할 줄 아는 사람이 늘어남
python.add("신영이")
print(python)

#java를 까먹었어
java.remove("김동현")
print(java)