# def add(x,y):
#     return x+y
# # 가변 매개 변수 *
# def makepizza(*topping):
#     print("다음 피자는 아래의 토핑이 들어갑니다")
#     for x in topping:
#         print(x)
#
#      makepizza("pineapple")
# #      makepizza(*topping: "pineapple","cheese")
# #      makepizza(*topping: "pineapple","cheese", "mushroom")
# def zodiac(*years):
#     symbols = ('닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀','말','양', '원숭이', '닭')
#     return [symbols[x-1993]for x in years]
# a=zodiac(*years())
# print(a)