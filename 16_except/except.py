#print(10/0)
from pprint import pformat

from pandas.conftest import index

# try: #오류 방지하기 위해
#     print(10/0)
# except:
#     print("예외 발생!")
#
# num = int(input("숫자를 입력해 주세요:"))
# print(10/num)
#
# try:
#     num = int(input("숫자를 입력해주세요: "))
#     print(10/num)
# except ValueError: #값 데이터 오류
#     print("문자말고  숫자 넣으쇼")
# except ZeroDivisionError:
#     print("0말고 딴거 넣으쇼")

#IndexError, ValueError
# file = None
# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트에서 가져올 인덱스:"))
#     print(my_list[index])
# except ValueError:
#        print("숫자만 입력해라")
# except IndexError:
#     print("그런 인텍스는 없음")
#
# #파일 입출력 예외 처리: FileNotFoundError 여기 다시 해보기
# try:
#     file = open("hi_txt", "r", encoding="utf-8")
#     content = file.read() #파일의 내용을 읽어온다.
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("그런 파일은 없어용")
# finally:
#     if file is not None and not file.closed:
#        file.close()
#         print("정상적으로 파일이 닫혔습니다.")
#     elif file is None:
#         print("애초에 열리지 않았습니다.")

#리스트 요소 5개 선언하고 index로 찾는 로직
#IndexError, ValueError 예외 처리
#정상적인 해당 리스트 값 출력
#마지막은 항상 끝!! 출력
#  my_list = [1, 2, 3, 4, 5]
#  try:
#     index_input = input("인덱슬르 입력하세요.")
#     index = int(input(index_input))
#     result = my_list[index]
# except IndexError as message:
#     print("해당 인덱스가 없습니다.")
#     print(message)
# except ValueError as message:
#     print("숫자를 입력하세요")
#     print(message)
# else:
#     print(f"해당 인덱스의 값 : {result}")
# finally:
# print("끝!!")

#raise 키워드 : 강제로 예외 발생시키기
#특정조건에서 개발자가 직접 예외를 발생시키는데 사용
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise  Exception("0이상 150미만 숫자만 입력하세요.")
# except Exception as e:
#     print(e)
# else:
#     print(f"입련된 나이 : {age}")
# finally:
#     print("끝!")
#커스텀 예외 클래스
#예외를 직접 만듦

#사용자 정의 예외 클래스
# class AgeException(Exception):
#     def __init__(self):
#         super().__init__("0이상 150미난 숫자만 입력하세요.")
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise AgeException()
# except AgeException as e:
#     print(e)
# else:
#     print(f"입력된 나이 : {age}")
# finally:
#     print("끝!")

#출금을 할때 잔액이 부족하면 발생되는 예외
#FundsError => 잔액이 부족합니다. 현재 잔액 ***원 , 출금 시도 금액 ***원
#Account 클래스 만들고 메소드 withdraw 출금
#출금을 할 때 잔액이 부족하면 FundsEroor를 발생
class FundError(Exception):
    def __init__(self, blance, amount): #생산자에서 현재

        super().__init__(f"잔액이 부족합니다, 현재 잔액{blance}원, 출금시도 금액 {amount}원")
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise FundError(self.balance, amount)
        except FundError as e:
            print(e)
        else:
            self.balance -= amount
            print(f"정상적으로 출금되었습니다. 남은 잔액: {self.balance}")

account1 = BankAccount(100000)
account1.withdraw(50000)
account1.withdraw(80000)

#딕셔너리 요소 찾기
#딕셔너리 키를 입력받음 (숫자로)
#result 변수에 해당 키의 값은 넣음
#예외처리 =>
#해당 키가 존재하지 않을 때 "KeyError" 처리: "해당 키는 존재하지 않습니다." 출력
#숫자가 아닌 문자를 입력 했을 때 'ValueError" 처리: "숫자를 입력해 주세요." 출력
#마지막으로 항상 "완료!!"를 출력

