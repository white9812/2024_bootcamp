
# prime number
number=int(input("Input number : "))
cnt=0

i=2
while i< number: #1과 자기자신은 돌지않음
    if number % i == 0:
        cnt=cnt+1
        #print(i) 약수 구하기
    i+=1 #무한 루프에 빠지지않기위해
if cnt ==0:
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")


#0의 의미=subjects format안에 첫번째 인수라는 것 응용하면 dictionary 여러개 쓸 수 있음
#소수
#count변수하나 저장하고 나누어떨어지는 횟수가 2번이면 소수
