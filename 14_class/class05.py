#Account 클래스 => 계좌 정보
#owner 그리고 balance => 잔액은 생성될 때 0으로 초기화
#deposit 입금 메소드를 추가하여 잔액을 증가 시키고 증가된 잔액을 출력
#withdraw 출금 메소드를 추가하여 잔액을 감소 시키고 감소된 잔액을 출력
#만약 잔액이 부족하다면 출금할 수 없돋록 출력

class Account:
     def __init__(self, owner, deposit, withdraw):
         self.owner =owner
         self.deposit = deposit
         self.withdraw = withdraw

     def blance(selfs):
         print(f"")
