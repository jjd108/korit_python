#반복문 (for)
"""
for 변수 in 반복할대상:
    반복할 코드
"""
from collection.didctionere import score

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
# a_tuple = ("안녕", "하세요", "반갑습니다")
# for a in a_tuple:
#     print(a)
#
# #세트 순희
# a_set = {"사과", "바나나", "체리", "딸기", "오렌지"}
# sorted_a_list = sorted(a_set )
# for a in a_set:
#     print(a)
#
# #세트 정렬 추가 설명
# numbers = {3, 1, 4, 1, 5, 9, 2}
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(type(sorted_numbers))
#
# word = "pythoon"
#
# for char in word:
#     print(char)
#
# for i in range(5):
#     print(i)
#
# for i in range(2, 10, 2): #2부터 10 미만까지, 2씩 증가
#     print(i)
#
# for i in range(1, 10):
#     print(i)
#     if i == 5:
#         print("i가 5입니다. 정지!")
#         break
#
# for num in range(1, 10):
#     if num == 5:
#         continue
#         print(num)
#
# #실습문제
# #1부터 100까지 짝수만 출력하기 (rage)
# for a in range (2, 101, 2):
#     print(a)
#
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)
#
#실습문제
#리스트의 합 구하기
# num = [10, 20, 30, 40, 50]
# total = 0

# for num in number:
#     total += num
# print("리스트의 합: ", total)

# for dan in range(1, 10):
#     for n in range(1, 10):
#         print(f"{dan} x {n} = {dan * n}")
#
# #평균 구하기
# scores = [80, 90 ,75, 88, 92]
# total = 0
# for score in scores:
#     total += score
#
# average = total / len(scores)
# print("평균점수: ",average)