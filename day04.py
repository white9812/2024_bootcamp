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
            else: #소수가 아닐때 계속 돌아간다.
                i=2
                while i*i <number: #그냥 i를 i*i로 하였음 소수가 아닌 수도 처리했지만 소수인 수도 반복문의 횟수를 줄임

                    if number % i == 0:
                        is_prime = False
                        break
                    i=i+1 #for문 때문에 자동 따라서 제거한다.
                    #print(i) 성능체크하려고 넣은것
                if is_prime:
                    pass
                    print(number, end=" ")
        print()#print자체에 줄바꿈기능있음