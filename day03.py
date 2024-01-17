#1
for i in list[range(3,-1,-1)]:
    print(i)

#2
# 문제점1:소수가 아닐때는 반복문을 빠져나오지만 앞 수가 소수일때는 끊임없이 반복문을 반복한다.
#
guess_me= 7
number=1
while True:

    menu = input("1) Fahraenheit ->Celsius 2) Celsius -> Fahrenheit 3)one prime number :       "
                 "4) prime numbers:           5) Quit program:   ")
    if menu == "1":
        fahrenheit = float(input("Input Fahreheit : "))
        print(f"fahrenheit: {fahrenheit}F,Celsius: {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C")
        print()
    elif menu == "2":
        celsius = float(input("Input celsius : "))
        print(f"fahrenheit: {fahrenheit}F,Celsius: {(celsius * (9.0 / 5.0) + 32):.4f}C")
        print()
    elif menu == "3":
        number = int(input("Input number : "))
        is_prime = True
        if number < 2:
            print(f"{number} is NOT prime number")
        else:

            for i in range(2, number):
                if number % i == 0:
                    if_prime = False
                    break
                # i=i+1 for문 때문에 자동 따라서 제거한다.

            if is_prime:
                print(f"{number} is prime number")
            else:
                print(f"{number} is NOT prime number")
        print()
    elif menu == "4":
        numbers = input("Input number : ").split()  # list
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1 #tuple로 만들어주고 각각 값 할당 하기 (n2,n1)이 임시 tuple,packing되었음
        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                # pass
                continue  # 둘다 해도 된다. 하지만 아무것도 안쓰면 문법 에러난다.
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                # i=i+1 for문 때문에 자동 따라서 제거한다.
                if is_prime: print(number, end=" ")
        print()#print자체에 줄바꿈기능있음
    elif menu == "5":
        print("프로그램 종료합니다.")

    if guess_me > number:
        print("too low")
    elif guess_me < number:
        print("oops")


        break
    else:
        print("find it!")
        print(number)
        break

    number = number + 1
#3
guess_me=5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif (number ==
          guess_me):
        print("find it!")
        break
    else :
        print("oops")
        break