# def good()->list:
#     '''
#     chapter 9 things to do 9-1
#     :return: list
#     '''
#     harry_poter=input().split()
#     return harry_potter
#
# print(good())

def get_odds(n):
    for i in range(1,n+1,2):
        yield i
cnt=0
odds=get_odds(9)
for odd in odds:
    cnt=cnt+1
    if cnt ==3:
        print(f"Third number is {odd}")
        break