#for_compA(심화버전

# a= [x for x in range(1001)]
# print(a)
# a=[x for x in range(101)]
# print(a)
#
# b=[x for x in range(501)]
# print(b)
# c=[x for x in "m"]
# print(c)
# e=[x*2 for x in range(1,101)]
# print(e)
# f=[x**2 for x in range(1,11)]
# print(f)
# g=[x+5 for x in range(1,11)]
# print(g)
#for comprehension 조건문
#
#
# a=[x for x in fruits if x.count('a')>0]
# b=[x for x in fruits if x.count('b')==1]
# print(a)
# print(b)
# c=[x for x in fruits if len(x)>=6]
# print(c)
# a=['😁😁' if x%2==0 else x for x in range(1,101)]
# print(a)
#유저에게 머ㅏㄴㅇㄹ을 입력받고, 1~100까지 리스트를 출력하는데,
#n의 배수만 🍟을 표현하고 나머지는 숫자로 표현
#2. 과일리스트에서 5글자 이하이면 대문자로 바꿔서 출력하고 아니면 🐑
# fruits=['banana','grape','apple','orange']
# a= [x.upper() if len(x)<=5 else '🐑' for x in fruits]
# print(a)
# num=int(input("숫자를 입력하세요:"))
b=['🥟'if x%2==0 else x for x in(1,101)]
print(b)
d= [x*y for x in range(1,15) for y in range(1,15)]
print(d)
e= [x+y for x in ['apple','banana']for y in ['pie','bob']]
print(e)