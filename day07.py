class FlyingBehavior:
    def fly(self):
        return "하늘을 훨훨 날아갑니다~"
class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."
class JetPack(FlyingBehavior):
    def fly(self):
        return f"날개로 하늘을 훨훨 날아갑니다."

class SwimmingBehavior:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp,fly):
        self.__name = name
        self.hp = hp
        selp.fly=fly

    def set_fly_behavior(self,fly):
        self.fly=fly

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # magic method
    def __str__(self):
        return self.__name + " 입니다"

    def __add__(self, target):
        #return self.__name + " + " + target.__name
        return f"두 포켓몬스터 체력의 합은 {self.hp + target.hp}입니다."


class Charizard(Pokemon):
    pass

class Pikachu(Pokemon):
    def __init__(self,name,hp,fly):
        self.name=name
        self.hp=hp
        # self.fly=fly #일반적인 값이 아니라 자식을 받음 ,aggregation
        self.fly=NoFly()#composition-객체가 피카츄안에서 만들어짐,객체가 변수가 됨
        #피카츄객체가 다른 객체를 가지고 있는 것


    pass
# nofly=NoFly()
g1=Pikachu("피카츄",35,nofly) #lsp
wings=FlyingBehavior() #객체가 받은 class가 다름 각각 작동함
c1 = Charizard("리자몽", 120,wings)
# g1.swim()
print(g1.fly.fly())
print(c1.fly.fly())#fly가 가지고 있는 fly인스턴스
print(p1.fly.fly()) #피카추는 날 수 없지만 jetpack 있으면 날 수 있음 getter/setter로 날 수 있는 기능 넣기
print(g1)
print(c1)
print(g1+c1)
#print(g1+200)
p1.set_fly_behavior(JetPack())
print(p1.fly.fly())
p1=Pikachu("피카츄",35,nofly)