#내장함수
#파이썬에서 기본적으로 지원하는 함수 (Built-In-Function
#abs() : 숫자의 절댓값을 리턴하는 함수
from operator import index

print(abs(-10))
print(abs(-1.2))

#all ()
#all (x)는 반복 가능한 데이터 x를 입력값으로 받으면
#이 x의 요소가 모두 참이연 True, 거짓이 하나라도 있으면 False를 리턴
#모든 요소가 참인가?
num_list = [1, 2, 0, 4]
print(all(num_list))
num_list = []
print(bool(num_list))
#빈 리스트 같은 경우, 안에 어떤 요소도 존재하지 않는다.
#따라서 "거짓인 요소가 하나라도 있는가?" => "거짓인 요소가 없다"
#거짓인 요소가 없기 때문에 모든 요소가 참이라는 조건이 위배되지 않는다.

#any()
#any(x)는 반복 가능한 데이터  x를 입력값으로 받으면
#이 x의 요소가 하나라도 참이면 true, 요소가 모두 거짓이면 false
num_list = [1, 2, 0, 4]
print(any(num_list))
num_list = [0, 0, 0, 0]
print(any(num_list))

#chr()
#chr(i)는 유니코드를 넣으면 해당 문자로 리턴을 하는 함수
print(chr(97))
print(chr(44035))

#dir()
#객체가 지난 변수나 함수를 보여주는 함수
name = "pythom"
print(dir(name))

#divmod ()
#2개의 숫자 a, b를 입력받고 그리고 a를 b로 나눈 몫과 나머지를
#튜를 형태로 리턴
print(divmod(7, 3))

#enumerate()
#순서가 있는 데이터(리스트, 튜플, 문자열)를 입력받아서 인덱스 값을
#포함하는 enumerate 객체를 리턴
#인덱스와 값을 두개의 변수로 언팩
a_list = ["name", "age", "birth"]

for i, value in enumerate(a_list):
    print(f"{i+1}. {value}")

#eval()
#문자열로 구성되어 있는데 해당문자열을 실행하는 값이 필요할 때
a_str = "1 + 2"
print(eval(a_str))
print(eval("divmod(7, 2)"))

#filter()
#첫 번째 인수로 함수, 두번째 인수로 반복사능한 데이터
#그리고 반복가능한 데이터의 요소 순서대로 함수를 호출했을 때
#리던값이 참인것만 묶어서 리턴

def positive (x):
    return x > 0
print(list(filter(positive, [1, -2, 5, -3, 8])))

#hex()
#정수를 입력 받아 16진수 문자열로 변환하여 리턴하는 함수
print(hex(234))
print(hex(23))

#id()
#객체를 입력 받아서 고유 주솟값 (레퍼런스)를 리턴하는 함수
a = 3
print(id(a))

#map() 중요!
#map은 입력받은 데이터의 각 요소에 함수를 적용한 결과를 리턴하는 함수
def two_time(x):
    return  x * 2
print(list(map(two_time, [1, 2, 3, 4])))

#max()
#반복 가능한 데이터 중에서 최댓값을 리턴
num_list = [1, 2, 13, 15, 23, 18, 55, 17, 46]
print(max(num_list))

#min()
#반복 가능한 데이터 중에서 최솟값을 리턴
num_list = [1, 2, 13, 15, 23, 18, 55, 17, 46]
print(min(num_list))

#oct()
#oct는 정수를 8진수를 문자열로 바꾸어 리턴하는 함수
print(oct(34))

#open() 중요!
#open(파일이름, 모드)은 파일 이름과 모드를 입력받아
#파일 객체를 리턴하는 함수
# w: 쓰기 모드, r: 읽기 모드, a: 추가 모드
file = open("예시.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

# with open("예시. txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content) #close 안해도 됨, 일아서 닫힘

#ord() <=> chr()
#ord는 문자의 유니코드 숫자 값을 리턴하는 함수
print(ord("가"))
print(ord("a"))

#pow()
#첫번째 인수 두번째 인수만큼 거듭제고 한 값을 리턴
print(pow(3,10))
print(pow(2, 12))

#range()
#range(시작, 끝, 간격) for문과 함께 자주 사용
#반복 가능한 객체로 만들어서 리턴
print(list(range(5, 100, 5)))

#round()
#반올림
print(round(4.4))
print(round(8.9))
print(round(5.1284, 2))

#sum()
#합계를 구하는 함수
num_list = [123, 5820, 475, 863]
print(sum(num_list))

#실습 문제
date = ["apple", "banana", "cherry", "grape", "mango", "blueberry","lamon"]
#1. apple
#2. banana
# 인덱스가 짝수인 요소만 출력 (인덱스: 요소)
for i, item in enumerate(date):
   if i % 2 == 0:
       print(f"인덱스: {i}, 값:{item}")



for i, value in enumerate(date):
    print(f"{i + 1}. {value}")

