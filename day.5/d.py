# # #1. 리스트의 기리 기능:len()
# # store=['c','g','s','m']
# # print(len(store))
# # #2. 리스트 추가:  append
# # store.append('emart')
# # print(store)
# # # store.insert(1.'familymart')
# # # store.insert(1. 'family')
# # # print(store)
# # # print(store)
# # #4. 리스트 제거: remove(what)
# # store.remove('c')
# # print(store)
# # #store.remove('c'
# # #5. 찾기 아이템 위치: index()
# # print(store.index('m'))
# # #리스트에 해당 아이템 세기: count
# # print(store.count('emart'))
# # #리스트 추가:익스텐드
# # newstore=['story','b']
# # store.extend(newstore)
# # # print(store)
# # # #리스트 정렬: sort
# # # store.sort()
# # # print(store)
# # # store.sort(reverse=True)
# # # print(store)
# # article="""(서울=연합뉴스) 성서호 기자 = 고물가가 이어지는 가운데 지난해 물가상승률이 반영돼 올해 국민연금, 기초연금 등 연금 수령액이 기존보다 3.6% 오른다.
# #
# # 국민연금은 지난해 역대 최고 수익률을 기록해 작년 수익금은 100조원, 기금 적립금은 1천조원을 넘어섰다.
# #
# # 보건복지부는 2024년도 제1차 국민연금심의위원회를 열어 연금액을 인상하고, 2024년에 적용하는 기준소득월액 상·하한액을 조정하기로 결정했다고 9일 밝혔다.
# #
# # 이에 따라 국민연금을 받는 약 649만명이 지난해 물가상승률(3.6%)만큼 오른 기본연금액을 이달부터 받게 된다."""
# # wordlist=article.split()
# # wordlist.sort()
# # print(wordlist)
# #key=중복 불가, 숫,문 타입 가능
# #value: 중복 가능 아무 타입
# zodiac={
#     1:'쥐',
#     2.:'소',
#     3.:'호랑이',
#     4.:'토끼',
#     5.:'용',
#
# }
# print(zodiac[4])
# mbti={'INFJ':'이상주의적',
#       'INTP':'과묵한',
#       'ESTJ':'깐깐한'}
# print(mbti['INFJ'])
# print(f"당신은 {mbti['ESTJ']}이시군요")
insta={'신촌 맛집':['싸다 김밥','순댓국','서브웨이'],
       '서강대 맛집':{'서강대 학식':['한식 정식', '양식' ,'일식' ]}}
print(insta["신촌 맛집"][2])