# #질문1
# def a(n1,n2):
#     print(n1,n2)
# def a(n):
#     print(n)
#
# a(7)
# a(7,11)
# #파이썬은 overloading개념이 없음 자바나 c++은 알아서 입력받은 값의 개수에 따라 알아서 함수 돌림
# #질문2
def a(n):
    if n is None:
        print(f"{n} is None")
    elif n:
        print(f"{n} is True")
    else:
        print(f"{n} is False")
a(None)
a("")
a(-9)
a([])
a([0])

