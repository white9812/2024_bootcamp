#subjects=["a","b","c"]
subjects=["a",["b","c"],"d"]
a=subjects
b=subjects.copy()
c=list(subjects)
d=subjects[:]
print(subjects,a,b,c,d)
#subjects[1]="x"
subjects[1][1]="x"
print(subjects,a,b,c,d)

import copy

#subjects=["a","b","c"]
subjects=["a",["b","c"],"d"]
a=subjects
b=copy.deepcopy(a)
c=list(subjects)
d=subjects[:]
print(subjects,a,b,c,d)
#subjects[1]="x"
subjects[1][1]="x"
print(subjects,a,b,c,d)
