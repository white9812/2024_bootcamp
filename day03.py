#1
for i in range(3,-1,-1):
    print(i)

#2
guess_me= 7
number=1
while True:
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