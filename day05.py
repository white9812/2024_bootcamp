# def out_func(nout):
#     def inner_func(nin):
#         return nin*nin
#     return inner_func(nout)
#
# print(out_func(5)) <- 일반적인 함수 호출


#closure는 바깥쪽의 함수의 인수를 그냥 바로 쓴다.
def out_func(nout):
    def inner_func():
        return nout*nout #직접 쓴다.
    return inner_func

x=out_func(9)
print(type(x))
print(x)
print(x())

