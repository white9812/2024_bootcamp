t9=1,21,3
t10=1,2,3,4
print(t9>t10)#순서대로 하나씩 비교
subjects=["c++","Java","python"]
print(subjects[::-1])
print(subjects)#원본이 바뀌진 않았음 할당을 한것은 아니라서
subjects.reverse()#원본자체를 바꿈
print(subjects)
subjects=subjects[::-1]
print(subjects[::-1])
subjects=["c++","Java","python","Java"]

#subjects.remove("Java")
#print(subject)
#subjects.pop(2)

subjects.sort()
print(subjects)
subjects.sort(reverse=True)
print(subjects)
subjects=["c++","Java","python","Java","5","9"]
print(subjects)
subjects.sort()
print(subjects)
subjects=["c++",5,"Java","python",1,"Java"]
a=[1,2,3]
b=a.copy()
