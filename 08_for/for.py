#반복문 (for)
"""
for 변수 in 반복할대상:
    반복할 코드
"""
# from idlelib.outwin import file_line_progs
#
# #리스트 순회
# frults = ["사과", '바나나', "딸기", "포도"]
#
# for fruit in frults:
#     print(fruit)
#
# scores = {
#     "alice": 85,
#     "bob": 92,
#     "charlie": 78}
# for key in scores: #키를 빼와서 변수에 할당
#         print(key,"의 점수는", scores[key])

#튜플 순회
a_tuple = ("안녕", "하세요", "반갑습니다")
for a in a_tuple:
    print(a)

#세트 순희
a_set = {"사과", "바나나", "체리", "딸기", "오렌지"}
sorted_a_list = sorted(a_set )
for a in a_set:
    print(a)

#세트 정렬 추가 설명
numbers = {3, 1, 4, 1, 5, 9, 2}
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(type(sorted_numbers))