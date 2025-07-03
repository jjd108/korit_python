# #list
# fruits =["apple"," banana", "cherry"] #문자열 리스트
# numbers = [1, 2, 3, 4, 5] #숫자 리스트
# mixed_list = ["안녕하세요", 42 , 3.14, "python"] #혼합사용가능하다
#
# 요소 접근 (인텍스)
# print(fruits[0])
# print(fruits[0][0])
# print(numbers[-1])
#
# #요소 접근 (인텍스)
# fruits[1] = "blueberry"
# print(fruits)
#
# #요소 추가
# fruits.append("grape") #마지막에 추가
# fruits.insert(__index1, __object"mango")
# print(fruits)
#
# #리스트 더하기
# list1 = ["A", "B", "C"]
# list12 = ["D", "E"]
# print(list1+list12)
#
# #리스트 곱하기
# print(list1 *3)
#
# #리스트에 여러 요소 추가
# list1.extend(list12)
# print(list1)
#
# #요소 삭제
# fruits.remove("cherry")
# fruits.pop()
# del fruits[2]
# print(fruits)
#
# #리스트 길이
# print(len(fruits))
#
#
# #리스트 슬라이싱
# print(numbers[1:4])
# print(numbers[::-1])
#
# #리시트 정렬
# numbers.sort() #기본적으로 오름차순 정력
# print(numbers)
#
# list1.sort(reverse=True)
# print(list1)
# kor = ["가", "나", "다"]
# kor.sort(reverse=True)
# print(kor)
#
#
# numbers2 = sorted(numbers) #원본 변수에는 영향이 없다, 새롭게 변수에 값을 할당
#
# #요소 존재 체크
# print("apple" in fruits)
#
# #리스트 요소를 이어 붙이기
# result = "-".join(list1)
# print(result)
from itertools import product

# #리스트 실습
# cart = []
# #3개의 상품명을 입력받아서  cart에 추가
# #최종적으로 cart를 출력
#
# product1 =input("추가할 상품 : ")
# cart.append(product1)
#
# product2 = input("추가할 상품 : ")
# cart.append(product2)
#
# product3 = input("추가할 상품 : ")
# cart.append(product3)
#



#튜플
colors = ("red", "blue", "green")
numbers = (1, 2, 3, 5, 9)
mixed = ("pink", 1, True)
single_tuple = ("hello",) #요소가 하나일 때는 꼭 ,를 붙여야 함
alphabet = ("a", "a", "a","b", "c", "c")

# #요소 변경 불가!!
# colors[1] = "yellow"

#튜플 슬라이싱
print(colors[:2])
print(colors[::-1])

#cont
print(alphabet.count("a"))
 #index
print(alphabet.index("b"))

#듀플 언패킹
a, b, c = colors
print(a, b, c)

