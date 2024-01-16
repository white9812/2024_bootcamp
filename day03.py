#index는 -1반환하지않음 따라서 예외처리 필요
#index의 return값으로 뭔가 하려고 하면 안됨
subjects="pythoncdatabaselinux"
print(subjects.isalnum())
print("%e"%0.7045)
print("%d%%"%100) #%자체를 쓰고 싶다.

subject =input("수강신청과목 입력 : ")
try:#여기서 예외가 터진다면
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스 ")
except ValueError:#여기서 해결
    print("해당 과목이 존재하지 않습니다.")
