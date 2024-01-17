#dictionary
#sugang={}

sugang=dict(python="kim",cpp="sung",db="kang")
# print(sugang)
# sugang['datastructure']="kim" #add
# print(sugang)
# sugang['datastructure']='park' #update
# print(sugang)
# print(sugang["db"])
# print(sugang.get('db'))
# print(sugang.get('opensource'))
# print(sugang.get('opensource','not exist'))
for subject,professor in sugang.items():#key, value동시에 뽑아줌 unpacking해서 찢은거
    print(f"{subject} 과목 담당교수는 {professor}입니다.")#현재 이 순서는  보장된 것이 아니다. 일부러 맞춘것


#for k in sugang.keys():
for k in sugang:#key는 default값
    print(k)
for v in sugang.values():#valus값만 뽑음
    print(v)
for s in sugang.items():
    print(s) #tuple형태로 묶여져서 출력


