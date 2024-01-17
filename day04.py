t1=(5)#이건 tuple이 아님. 그냥 integer에 소괄호가 쓰여져있음
t2=5,
t3=(5,)
t4=(5,7)
t5=5,7
print(type(t1),type(t2),type(t3),type(t4),type(t5))
#소괄호를 쓰지않아도 tuple을 만들 수 있다.
t6="python","kim" #packing -,사용하면 담는 역할을 함,
print(type(t6),t6[1])
#2개를 동시에 담을 수 있음
subject,prof =t6
print(prof) #unpacking, 순서대로 subject,prof에 들어감 주의사항:갯수가 맞아야됨
#a,b,c=t6 #ValueError: not enough values to unpack (expected 3, got 2)
print(subject)
t7=()
t8=tuple()
print(type(t7),type(t8),type(9,),type((9,)))#type(9,)에서 ,는 type의 부분으로 인식
t9=1,2,3
t10=1,2
print(t9==t10)
print(t9 <= t10)
print(t9 < t10)
print(t9>t10)
t11=4.43, #tuple로 만들려면 입력값 하나일때 ,필수
t12=3.97,4.1,3.27
print(id(t11))
print(t11+t12)


t11=t11+t12
print(t11)
print(id(t11))

