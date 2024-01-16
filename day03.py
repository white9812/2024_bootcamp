course ="2024 KEB bootcamp"
print(course.replace("KEB","Inha"))
print(course)
course=course.replace("KEB","Inha")
print(course)
course="KEB 2024 KEB bootcamp"
course=course.replace("KEB","Inha",1)
print(course)
course="KEB 2024 KEB bootcamp KEB"
course=course.replace("KEB","Inha",2)
print(course)
course="KEB 2024 KEB bootcamp KEB"
course=course.replace("KEB","Inha",100)
print(course)
course="KEB 2024 KEB bootcamp KEB....*!#"
print(course.strip())
print(course.strip("!#.*"))
course="KEB# 2024 KEB bootcamp KEB....*!#"
print(course.strip("!#.*"))
course="* KEB# 2024 KEB !bootcamp KEB....*!#"
print(course.strip("!#.*"))
print(course.find("KEB"))
print(course.rfind("KEB"))
print(course.index("KEB"))
print(course.find("Inha")) #-1 if 문 사용 -1이면 찾으시는 문자열은 없습니다.
print(course.index("Inha"))#ValueError: substring not found

