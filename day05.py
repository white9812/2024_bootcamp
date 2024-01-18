# numbers= ["7","-11","3"]
# hap=0
# for number in numbers:
#     hap=hap+int(number) <-정수로 바꾸기 위해
# print(hap)

#더 간단한 방식
numbers= ["7","-11","3"]
print(map(int,numbers)) #객체로 나옴
print(sum(map(int,numbers)))#그냥 출력할땐 이렇게 쓰고 끝내면 됨

