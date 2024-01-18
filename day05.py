def squares(n):
    return n*n
even_numbers=[i for i in range(51) if i%2==0]
print(even_numbers)
print(map(squares,even_numbers))#map(func,sequnce type)
print(tuple(map(squares,even_numbers)))

# print(tuple(map(lambda x: x**2 ,even_numbers))) #익명함수 만듦  squares 필요없음, 익명함수도 함수임
z=lambda x:pow(x,2)
print(tuple(map(z,even_numbers)))
