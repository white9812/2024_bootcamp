# #class Poketmon():
# class Poketmon():
#     def __init__(self,names):#self는 자동으로 들어가는 매개변수임,그냥 s라고 해도 됨
#         print(f'{names} 포켓몬스터 생성') #메모리 위치주소를 self가 가지고 있음
#
# pikachu=Poketmon("피카츄") #해당 객체마다 __init__은 딱 한번만 돌아감
# squirtle=Poketmon('꼬부기')#__init__때문에 객체 초기화가 가능한 것
# print(pikachu)#class에 있는 객체인데 이 메모리에 있다.
# print(squirtle)

# class Pokemon:
#     pass
# pikachu=Pokemon()
# squirtle=Pokemon()
# #객체에 속성 할당
# pikachu.name="피카츄" #객체에 이름 속성을 부여하고
# pikachu.nemesis=squirtle
# print(pikachu.name)
# squirtle.name="꼬부기"
# print(pikachu.nemesis.name)
# print(squirtle.name)
#교수님 코드 다시보기
#human class의 객체
# 우리 모두 sleep기능 가지고 있음
# a학생이 잔다면 a객체라는 특수객체가 sleep을 동작시킴 이 객체가 self =누가 그 기능을 실행시키고 있는가?

class Poketmon(): #포켓몬에는 name이라는 속성을 가지고 있지않다.
    def __init__(self,names):
        self.name=names #이 한줄을 넣음으로써 속성 부여
        print(f'{names} 포켓몬스터 생성')
    def attack(self,target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
charizard=Poketmon("리자몽")
pikachu=Poketmon("피카츄") #피카츄가 꼬부기,속성을 필드라고도 한다.
squirtle=Poketmon("꼬부기")
print(pikachu.name)
charizard.attack(squirtle) #squirtle이  attack의 인수
#charizard가 self임
print(charizard.name)