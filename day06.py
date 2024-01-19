class Pokemon:
    def __init__(self,name):
        self.name=name
    def attack(selfself,target):
        print(f"{self.name}이(가)  {target.name}을(를) 일렉트릭 공격")
 class Squirtle(Pokemon):
     def attack(selfself, target):
         print(f"{self.name}이(가)  {target.name}을(를) 일렉트릭 공격")
     def electirc_info(self):
         print("전기계열의 공격을 합니다.")

p1=pikacu("피카츄")
p2=squritle("꼬부기")
p3=Pokemon("아무개")
p1.electric_info()
p3.eletric_info()
p1.attack(p2)
p2.

print(p1.name) # p1에 name없으니까 부모 클래스에 올라간다.
print(issubclass(Pickchu,Pokemon))
print(issubclass(Pickchu,Pokemon))

