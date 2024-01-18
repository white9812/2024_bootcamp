def my_range(first=0,last=10,step=1):
    number=first
    while number<last:
        yield number
        number +=step

r=my_range()
print(r,type(r))

for x in r:
    print(x)

for x in r:
    print(x) #generator걕체 이용했지만 이건 기억되지 않아서 숫자만 발생하고 한번 쓰고 삭제됨 따라서 다시 객체를 만들어야함



