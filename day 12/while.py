#while
#조건식이 특정 탈출 경우가 없으면 무한 반복
a=1
# while a<10:
#     print('아메리카노')
#     a+=10
# while True:
#     print("너가 숫자 1을 넣어야 탈출할 수 있다.")
#     num=int(input("숫자 입력:"))
#     if num ==1:
#         break
#while: 유저가 끝을결정 짓는 상황
#for: 프로그래머가 끝을 결정 짓는 상황
coffeelist=[] # 데이터 베이스, 엑셀에서 가져오는 데이터 코드
while True:
       print("메가커피 프로그램")
       print("1.커피 등록하기")
       print("2.커피 메뉴보기")
       print("3.시스템 종료")
       coffee=int(input("번호 입력:"))
       if coffee==1:
           print("커피 등록 시스템")
           name=input("커피 이름 입력:")
           coffeelist.append(name)
           print("등록 완료")
       elif coffee==2:
           if len(coffeelist)== 0:
               print("커피 메뉴가 없습니다")
           else:
               print(coffeelist)
       elif coffee==3:
           print("이용해 주셔서 감사합니다")
           break
       else:
           int(input("숫자를 다시 입력하세요:"))