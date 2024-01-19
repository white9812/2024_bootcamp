
#데코레이터니까 인수가 있어야함
def test(f):
    '''
    데코레이터 함수, 함수 시작하면 start출력, 함수 끝나면 end출력
    :param f: function
    :return: closure function
    '''
    def test_in(*args,**kwargs):#비워서 해도 되지만 필요한 값이 있으면 인수 넣어주기
        print("start")
        result=f(*arges,**kwargs)
        f()
        print("end")
        # return result
    return test_in

def greeting():
    print("안녕하세요~")
    #수정하진 않고 확장에는 열려있음
#인수없으니까 바로 greeting?호출
t=test(greeting)

