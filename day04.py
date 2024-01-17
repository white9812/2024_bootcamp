#assignment
#1
e2f={"dog":"chien","cat":"chat","walrus":"morse"}
print(e2f)
#2
# print(e2f.keys("walrus")) 에러난 이유:keys()는 모든 key값을 가지고 오는 것
print(e2f["walrus"])
#3
# f2e_list=list(e2f.items())[::-1]
# f2e_list=list(e2f.items()).reverse() 둘다 같은건데 왜 안되는지 모르겠음
# f2e_list.reverse()
# print(e2f.items())
print(e2f.items()) #이거 자체는 dict_items()
k=e2f.items()
print(type(k)) #TypeError: 'dict_items' object is not subscriptable(인덱싱 또는 슬라이싱  불가)
# for e ,f in  list(e2f.items()):
#    print(e,f) ->생각해보기
#ver1
f2e={}
for pair in list(e2f.items()):
    #print(type(pair))
    e=pair[0]
    f=pair[1]
    #new_pair={f:e}
    f2e.update({f:e})
print(f2e)
#ver2->이게 더 나음
f2e={}
for e, f in list(e2f.items()):
    f2e.update({f:e})
    print(f2e)
#ver3 update없이 바로 넣는 방법은 없을까?

#4
#ver1
print(list(e2f.keys())[list(e2f.values()).index("chien")])
#type(e2f.values())
#<class 'dict_values'> =>큰 dict에 유용, 사용하지 않을 list를 만들지 x
#ver2 value와 key값을 바꿔서 찾음
print(f2e["chien"])
#ver3 반복문이용- 그런데 이방식은 v가 chien인거 찾을때까지 계속 돌아감
for k, v in e2f.items():
    if v=="chien":
        print(k)

#5
for e in e2f.keys():
    print(e)

#6 참조= 이름이 같다.
life={
    "animals":{"cats":"Henry","octopi":"Grumpy","emus":"Lucy"},
    "plants":{},
    "other":{}
}

#7
print(list(life.keys()))

#8
print(list(life["animals"].keys()))

#9
print(life["animals"]["cats"])
#10
squares={i:i*i for i in range(10)}
print(squares)

#원본 교재
#6
# "animals"{"cats":"Henry","octopi":"Grumpy","emus":"Lucy"} <-SyntaxError: invalid syntax
#
life={
    "animals":{"cats":["Henry","Grumpy","Lucy"],"octopi":" ","emus":" "},
    "plants":{},
    "other":{}
}
#7
print(list(life.keys()))

#8
print(list(life["animals"].keys()))

#9
print(life["animals"]["cats"])
#10
squares={i:i*i for i in range(10)}
print(squares)



