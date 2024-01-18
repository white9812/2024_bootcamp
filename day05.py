def is_prime(n) -> bool:
    """
    매개변수로 넘겨받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True,아니면 False
    """
    #is_prime=True <- 굳이 필요 없음
    if n<2:
        return False
    else:
        i=2
        while i*i<=n:
            if n %i ==0:
                #is_prime=False
                #break 함수탈출은 return원래꺼 필요없음
                return False
            i+=1
        return True


# help(is_prime)
# help(len)


numbers = input("Input number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1
for number in range(n1, n2 + 1):
    if is_prime(number):
        print(number, end=" ")

