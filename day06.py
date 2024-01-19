#recursion(재귀)
def factorial_repetition(n)->int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: 정수,int
    :return: 팩토리얼 값,int
    '''
    result =1 #곱셈에 대한 연산을 할거라서
    for i in range(2,n+1):
        result =result*i #값이 변할 위험성이 있음 따라서 이런경우 재귀함수가 유용 하지만 좀 느림
    return result
def factorial_recursion(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수,int
    :return:  function,int
    '''
    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1) #n=1이 될때까지 반복
number=int(input("number: "))
# print(factorial_repetition(int(input("number : "))))
print(factorial_recursion(number))
