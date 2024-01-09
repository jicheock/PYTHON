#+:str+str:=문자
#int: 사칙연사
#list: 리스트 연결 연산
coffee=['아메리카노', '라떼', '바닐라']
cookie=['화이트 쿠키','녹차']
menu=coffee+cookie
print(menu)
double_menu=menu*2
print(double_menu)
print('아메리카노' in menu)
print('마요네즈' in menu)
new_menu=menu[1:4]
print(new_menu)