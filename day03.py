
# prime number
number=int(input("Input number : "))
is_prime=True
if number <2 :
    print(f"{number} is NOT prime number")
else:

 for i in range(2,number):
        if number % i == 0:
            if_prime = False
            break
        #i=i+1 for문 때문에 자동 따라서 제거한다.


    if is_prime:
        print(f"{number} is prime number")
    else:
        print(f"{number} is NOT prime number")

# 구간 입력받기
# prime number
numbers=input("Input number : ").split() #list
n1=int(numbers[0])
n2=int(numbers[1])

if n1>n2:
    n1,n2 =n2,n1
for  number in range(n1,n2+1):


    is_prime=True
    if number <2 :
        pass

    else:
        for i in range(2,number) :
            if number % i == 0:
                if_prime = False
                break
        #i=i+1 for문 때문에 자동 따라서 제거한다.
        if is_prime: print(number,end=" ")


