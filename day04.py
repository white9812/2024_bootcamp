# drink_food={"위스키":"초콜릿","와인":"치즈","소주":"삼겹살","고량주":"양꼬치"}
#
# drink=input(drink_food.keys())
# dringk_kejs
# #drininput("다음 둘 중에 고르시오")
# drink=input(d)
#
# print(drink_food[drinks])

import random
drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}

#drink = input(drinks_foods.keys())
drinks_foods_keys = list(drinks_foods)
#print(drinks_foods_keys)
#print(random.choice(drinks_food_keys))#sequence type의 값은 리스트가 아니여도 된다. 여기서 하나 선택
#random_drink=random.choice(drinks_foods_keys)
while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) 랜덤 6) 종료 : ')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
    elif menu == '5':
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]5} 입니다.')
        print(f'다음에 또 오세요')
        pass
    elif menu == "6":
        print(f'다음에 또 오세요')

        break