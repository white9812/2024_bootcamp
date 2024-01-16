
# prime number
number=int(input("Input number : "))
is_prime=True # 공간을 줄임 int -> bool

i=2
while i< number: #1과 자기자신은 돌지않음
    if number % i == 0:
       if_prime = False #remove +
        break
    i+=1

#if cnt ==0: #remove ==
if is_prime:
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")
