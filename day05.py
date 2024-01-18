#assingment
#1
def good():
    return print(["Harry",'Ron',"Hermione"])
good()
#2
def get_odds(first=0,last=10,step=1):
    number = first
    while number < last:
        if number % 2==1:
            yield number
        number+=step
ranger=get_odds(1,10,1)
for x in ranger:
    print(x)

#3
def test(func):
    result=func()
    print()
