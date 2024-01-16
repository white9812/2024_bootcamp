university=("Inha\nUniversity!")
#print(university)
print(university[:4])#정방향
print(university[:-11])
print(len(university))
print(university[::2])
print(university[::1])

#university=r"Inha\nUniversity"#raw string-tab키나 줄바꿈을 그대로 보여줌
#print(university)
number1=input("First number: ")
number2=input("Second number: ")
print(number1+number2)#산수가 아니라 문자열끼리 결합
print(number1*3)
print(number1+3)#TypeError: can only concatenate str (not "int") to str

