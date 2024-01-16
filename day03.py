
# prime number
number=int(input("Input number : "))
is_prime=True
if number <2 :
    print(f"{number} is NOT prime number")
else:

 for i in range(2,number)
        if number % i == 0:
            if_prime = False
            break
        #i=i+1 for문 때문에 자동 따라서 제거한다.


    if is_prime:
        print(f"{number} is prime number")
    else:
        print(f"{number} is NOT prime number")
