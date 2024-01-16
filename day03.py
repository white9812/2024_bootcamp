univ="inha"
i=0
while i<len(univ):
    print(univ[i],end=" ")
    i=i+1
#바로 위 코드는 오류날 수 도 있음
print()

# best
for letter in univ:
    print(letter,end=" " )

print()

#for k in range(0,len(univ),1): #1생략가능
#for k in range(0,len(univ),1):
# best
for k in range(len(univ)):
    print(univ[k],end=" ")