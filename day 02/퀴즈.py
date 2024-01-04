# useryear =int(input("몇 년 생이냐:"))
#
# print(f"귀하의 나이는 만 {2023 -useryear} 이구나")
# print(f"귀하의 나이는 만 {2023 /useryear} 이구나")
# a = float(input("첫 번째:"))
# b =float(input("두 번째:"))
# c =float(input("세 번째:"))
# sum = a+b+c
# avg =sum/3
# print(f"총합: {sum}, 평균:{avg}")

#3) 섭씨 온도를 입력받아 화씨로 출력
# F= C*5.932
C=int(input("오늘의 온도:"))
F= C*5.9+32
#변수 .2f= 둘째 자리까지 정래

print(f"오늘의 화씨 온도는{F: .2f}구나!")
#4) Bmi 출력 =(weight/height**2)-->키 몸 입력받기 먼저
kg=float(input("너의 몸무게:"))
h=float(input("너님의 키:"))
BMI = kg/(h**2)
print(f"너의 BMI는 {BMI:.2f}구나")
#5)반지름 입력시 원의 둘레와 넓이를 구하는 프로그램
r=int(input("원의 반지름:"))
width = 3.14*r*r
round = 2*3.14*r
print(f"원의 넓이:{width} 원의 둘레:{round:.2f}")

#print() = 출력
#input()= 입력[결과: 문자 타입]
#변수- 임시 저장
# int(), float(), srt()
# 사칙연산 -,+,*,/,%,**