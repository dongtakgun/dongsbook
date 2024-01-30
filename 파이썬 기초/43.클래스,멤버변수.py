#42.클래스를 클래스로 만든 거임


class unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0} 공격력 {1}".format(self.hp,self.damage))

# marine1 = unit("마린",40,5)
# marine2 = unit("마린",40,5)
# tank= unit("탱크",150,35)

# 레이스 : 공중 유닛, 비행기 . 클로킹

wraith1 = unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# 다크아칸이 마인드 컨트롤
wraith2 = unit("빼앗은 레이스",80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))