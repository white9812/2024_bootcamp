import random
class OopsException(Exception):
    pass
# numbers=list()
# for i in range(5):
#     numbers.append(random.randint(1,100))
# print(numbers)

numbers=[random.randint(1,100) for i in range(5)]
# print(numbers)
# pick=int(input("Input index: "))
# print(numbers[pick])
# pick=int(input(f"Input index(0~{len(numbers)-1}): "))
# print(numbers[pick])

#예외처리하자
try:
    pick=int(input(f"Input index(0~{len(numbers)-1}): "))
    print(numbers[pick])#index 에러는 여기서 발생하는 것
    print(5/2)
    raise OopsException("Ooops~~~") #마지막에 에러로 발생했을때 마지막 except Exception 발생
#강제로 에러를 만들었음 어디에도 해당하지 않는 경우에
#근데 except Oops~ 밑에 만들었을땐 거기에 걸림
# except IndexError : #그냥 except 하면 모든 에러 잡음 즉 index에러 아닌것도 이렇게 출력함
#     print("Out of range : Wrong index number")
except IndexError as err :
     print(f"Out of range : Wrong index number \n {err}") # 시스템에서 던져주는 에러메세지
# except ValueError:
#     print("Input Only Number~")
except ValueError as err: #꼭 err하지않아도 됨
     print(f"Input Only Number~\n {err}")
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0.\n{err}")
# except Exception: #맨 밑에 와야함
#     print("Error occurs")
except OopsException as err:
    print(f"Ooops {err}")
except Exception as err: #맨 밑에 와야함
     print(f"Error occurs \n {err}")
else:
    print(f"Program terminate")

