#부모 클래스 (Super Class)
from pydoc import describe


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 동물 객체 생성!")

    def speak(selfs): #부모 클래스의 speak 메소드를 제정의 (Over
        print("왈왈")

    def move(self):
        print(f"{self.name}이(가) 움직입니다.")

class Cat(Animal):
    def speak(selfs):
        print("애옹")

    def climd(self):
        print(f"{self.name}이(가) 높은 곳에 올라갑니다.")
#=========상속 시작========
#메소드 오브라이딩

#자식클래스 (sub class)
#괄호 안에 부모 클래스 이름을 명시해서 상속 선언
class Dog(Animal):
    def wag(self):
        print(f"{self.name}이(가) 꼬리를 흔듭니다.")

animal1 = Animal("일반 동물")
animal1.move()
animal1.speak()

dog1 = Dog("방울이")
dog1.speak()
dog1.move()
dog1.wag()

cat1 =Cat("냥냥이")
cat1.speak()
cat1.move()
cat1.climd()

# 실습
#shape 라는 부모 클래스 => color
#매소드 describe => 이 도형의 색깔은 *** 입니다. 출력

#circale 자식 클래스
#매소드 describe 오버라이딩 => 이 원의 색깔은 ***입니다. 출력
#매소드 get_area(radius) => math.pi 모듈을 이용해서 넓이 구해서 리턴
#리턴한것을 print로 출력할 때 소수점 둘째까지

import math
class Shape:
    def __init__(self, color):
        self.color =color

    def describe(self):
        print(f"이 도형의 색깔은 {self.color}입니다.")

    def describe(self):
        print(f"이 원형의 색깔은 {self.color}입니다.")

class Circle(shape):
    def get_area(self, radius):
        return  math.pi * (radius ** 2)

circle1 = Circle("빨간색")
circle1.describe()
print(f"원의 넓이: {circle1.get_area(5): 2f}")


