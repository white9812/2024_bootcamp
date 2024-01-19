def desc(f):
    def wrapper():
        print("study")
        f() #someething()저 wrapper안에서는 f가 뭔지 모름
    #print("a")
    return wrapper
#desc()
#wrapper는 독립적으로 존재  desc부른다고   wrapper가 돌아가지는 않음
# def desc():
#     def wrapper():
#         print("study")
#     print("a")
#     return wrapper
# 위 코드 돌려보기

def something():
    print("do something~")
something()
s=desc(something) #클로져가 f를 기억하고 있음 ,f는 밖에서 선언된 것
s() #이렇게 쓸 필요가 없음
@desc
def something():
    print("do something~")
something()