class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~ "
class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."
class Pokemon:
    def __init__(self,name):
        self.name=name
    def attack(self):
        print("공격!")

    def get_name(self):
        print("inside getter")
        return self.name

    def set_name(self,new_name):
        print("inside getter")
        self.name=new_name

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
print(g1.name) #<-직접적으로 접근
print(g1.set_name)#g1.setname()하면 에러남
g1.set_name("잉어킹")
g1.name="잉어킹"
print(g1.name)
