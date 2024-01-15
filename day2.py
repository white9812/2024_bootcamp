print(0.1)
print(1e-1)
print(0.01)
print(314e-2)
print(21_000)
univ = "Inha university"
# 주석 ctrl+/
print(univ)
print(univ[5])
# univ[5]=U
subjects = ['python', "C++", "linux", "data structure", "database"]
print(subjects)
print(subjects[3])
subjects[3] = 'data structure &algolithm'
print(subjects)
# 0k
abc = 7
Abc = 8
ABC = 6
# case-sensitive
print(abc, ABC, Abc)
test9 = 77
# 9test=77
_9test = 77
print(test9, _9test)
# False=123 #reserved words
x = 2
y = x + 5
print(y)
print(type(3.14) == float)
print(isinstance(3.14, float))
money = 5, 00, 00
print(money)
print(type(money))
base_number = int(input("input base number :"))
exponent_number = int(input("input exponent number :"))
print(f"밑은{base_number}, 지수는 {exponent_number}, 결과 값은 {base_number ** exponent_number}")
base_number = int(input("input base number :"))
exponent_number = int(input("input exponent number :"))
print("밑은{0}, 지수는 {1}, 결과 값은 {2}".format(base_number, exponent_number, pow(base_number, exponent_number)))
print("밑은{}, 지수는 {}, 결과 값은 {}".format(base_number, exponent_number, pow(base_number, exponent_number)))
# c언어 비슷하게
print("밑은 %d, 지수는 %d, 결과 값은 %d" % (base_number, exponent_number, pow(base_number, exponent_number)))
first_number = int(input("First number : "))
second_number = int(input("Second number : "))
quotient = first_number // second_number
remainder = first_number % second_number
print(f"몫은 {quotient},나머지는 {remainder}입니다.")
print(f"몫은 {divmod(first_number, second_number)[0]},나머지는 {divmod(first_number, second_number)[1]}입니다.")
# 성능은 연산기호 사용하는 것이 빠름


artists = ["BTS", "뉴진스", "핑클", "ses", "HOT", "블랙핑크"]
groups = artists
print(artists, groups)

artists[2] = "세븐틴"
print(groups)
dec = 65
octal = 0o101
hexadecimal = 0x41
binary = 0b01000001
print(dec, octal, hexadecimal, binary)
print(chr(dec), chr(octal), chr(hexadecimal), chr(binary))
print(ord("B"), ord('Z'), ord("a"), ord("2"))  # 66,90,97,50
fahrenheit = float(input("Input Fahreheit : "))
# (0°C × 9/5) + 32 = 32°F
print(f"fahrenheit: {fahrenheit}F,Celsius: {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C")
print(int("1A", 16))
menu = input("1) Fahraenheit ->Celsius 2) Celsius -> Fahrenheit 3)Quit program : ")
if menu == "1":
    fahrenheit = float(input("Input Fahreheit : "))
    print(f"fahrenheit: {fahrenheit}F,Celsius: {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C")
elif menu == "2":
    fahrenheit = float(input("Input Fahreheit : "))
    print(f"fahrenheit: {fahrenheit}F,Celsius: {(celsius * (9.0 / 5.0)) + 32:.4f}C")
else:
    print("프로그램 종료합니다.")

fahrenheit = float(input("Input Fahreheit : "))

print(f"fahrenheit: {fahrenheit}F,Celsius: {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C")
sum = 1 + \
      +2 \
      + 3 \
 \
    print(sum)

temp = []  # 비어있는 empty list는 false
# temp=[0]<-0이라는 원소가 존재하기에 비어있는 것이 아님,즉 이 자체가 True
if temp:
    print("원소가 존재")
else:
    print("비어있는 리스트")

# letter="k"
letter = input("Input alphabet letter: ")
print(type(vowels))
# vowels={"a","e","i","o","u"} set
vowels = "aeiou"  # str
if letter in vowels:  # in
    print(f"{letter} is a vowel~")
else:
    print(f"{letter} is a consonant!")
    l = [1, 3, 3, 2, 4]  # list 그냥 순서대로 나옴 sequence자료 타입이라서
    s = {1, 3, 3, 2, 5}  # set-> 중복값은 지움 ,set는 유니크. 둘다 자료값을 바꿀 수 있음

    print(l, s)
