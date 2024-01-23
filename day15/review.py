# def __init__(self,phone_number):
#    self.phone_number=phone_number
#    phone_number=int(input("핸드폰 번호를 입력하세요"))
# def __init__(self, solution):
#     self.solution=solution
#     if self.phone_number>4:
#         map(,self.phone_number)
#"123124523"
def solution(phone_number):
    NewNumber=""
    for index,item in enumerate(phone_number):
      if len(phone_number)-4>index:
          NewNumber+="*"
      else:
          NewNumber+=item
    return NewNumber
a=solution("4381290471324")
print(a)


