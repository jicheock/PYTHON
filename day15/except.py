try:#에러가 날 것 같은 구문을 적는 곳
      num=int(input("숫자 입력:"))
      result=10/num
      print(f"결과는 {result}")
except ValueError:
    print("숫자를 입력하세요")
except ZeroDivisionError:
    print("0으로 못 나눈다")
else:
    print("임무 완료")
finally:
    print("상관없으니 보여줘라")
