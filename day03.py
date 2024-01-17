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
            n1, n2 = n2, n1
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
        break
