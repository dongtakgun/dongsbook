#튜플은 리스트와 다르게 추가 수정이 불가능하다. 대신 리스트보다 속도가 빠름


menu = ("돈까스","치돈")

print(menu[0])

# menu.add("생선까스") > 불가능

# name = "김종국"
# age = 20
# hobby = "코딩"

# print(name,age,hobby)

(name,age,hobby) = ("김종국",20,"코딩")
print(name,age,hobby)