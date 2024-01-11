# numbers=int(input("숫자를 입력하시오:"))
# if numbers%2==1:
#     print("홀수입니다")
# else: print("짝수입니다")
# code=input("코드를 입력하세요:")
# if code.isupper():
#     print("알파벳 포함")
# else: print("알파벳이 없네욬ㅋㅋ")
# pw=input("코드를 입력하세요")
# if len(pw)<10:
#     print("비밀번호는 10자 이상이어야 합니다")
# elif pw.isalnum() or ('in' in pw or'@'in pw or '#'in pw or '$'in pw):
#     print("영어와 숫자를 꼭 포함해 주세요")
# else:
#     if not ('in' in pw or'@'in pw or '#'in pw or '$'in pw):
#         print("특수문자를 포함해주세요!@$$#")
#     else:
#         print("비밀번호 설정 완료")
#

bus={
    1.:{'name': '시내버스',
        'price': 1200,
    },
    2.:{'name': '마을 버스',
        'price':'13\500'},
    3.:{'name': '마을 버스',
        'price': 1000}
}
bus_choice= int(input(f"버스를 선택하세요!! :[1. 시내버스-1200, 2. 광역버스-1500, 3. 마을 버스-1000] "))
print(f"버스")
age=int(input("나이를 입력하세요:"))
if age<=7or 65 <=age:
    print('')
elif 8<=age and age<=19:
    print(f"{bus[bus_choice]['name']}의 {bus[ bus_choice]['price']*0.7}가격 입니다")
else:
    print(f"{bus[bus_choice]['name']}의 {bus[ bus_choice]['price']}가격 입니다")


