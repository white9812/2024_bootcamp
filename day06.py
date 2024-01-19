class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~ "
class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."
class Pokemon:
    def __init__(self,name):
        self.__name=name
    def attack(self):
        print("공격!")
    @property
    def name(self):
        print("inside getter")
        return self.__name
    @name.setter
    def name(self,new_name):
        print("inside getter")
        # self.name=new_name 왜 오류나는지 모르겠음
        self.__name = new_name

    # name=property(get_name,set_name)

class Charizard(Pokemon,FlyingMixin):
    pass

class Gyarados(Pokemon,SwimmingMixin):
    pass

g1=Gyarados("가라도스")#객체생성
c1=Charizard("리자몽")
# print(c1.fly())
# print(g1.swim())
# c1.attack()
#Charizard.attack()#c1안주면 에러남 클래스명을 준것=Charizard.한것 자체가
#self에는 객체명이 와야함 따라서 c1(self)가 와야함
# print(g1.name) #<-직접적으로 접근
# print(g1.set_name)
# #g1.setname()하면 에러남
#print(g1.get_name())
# g1.set_name("잉어킹")
# g1.name="잉어킹"
#property
# print(g1.name) #property name으로 불러옴
g1.name="잉어킹"
g1.hidden_name="잉어킹"
g1.__name="잉어킹"#에러 값이 안들어감
g1._Pokemon__name="잉어킹"
#실질적으로 파이썬에는 접근 제한이 없음 ,접근 제한 하려면 숨기고 싶은 속성에 __하면 됨
print(g1.name)
# print(g1.__name) #direct access X
print(g1.hidden_name)
print(g1._Pokemon__name) #사실상 private 개념은 없는 걸로 그냥 우회한것
##__바로 접근 안됨 property직접접근안되니까 .name으로 접근,,?
