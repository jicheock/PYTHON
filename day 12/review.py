# # num=int(input("숫자를 입력하세요:"))
# # #
# # # for x in range(100):
# # #     if x%num==0:
# # #      print(x)
# # num=int(input("숫자를 입력하세요:"))
# # for x in range(1,10):
# #        print(f"{num}*{x}")
# break: for, while 반복 끊는 역할
# continue: jump 같은 역할

for x in range(100):
    if x ==50:
        continue
    else:
        print(x)