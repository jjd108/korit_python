#person => age, email, name /// name은 기본값으로 홍길동
#introduce 메소드 =>  자신을 소개하는 메소드

class person:
    def __init__(self, age, email, name = "홍길동"):
        self.age = age
        self.email =email
        self.name = name

    def introduce(self):
            print(f"이름은 {self.name}이고 나이는{self.age}, 이메일은{self.eamil}")

        person = person(00, "gksfm92214@naver.com", "jjd")
        person.introduce()

        person2 =person(20, "gksfm92214@naver.com")
        person2.introduce()

        person2.address = "서울" #person2 객체에 address라는 새로운 속성을
        print(person2.address)

        setattr(person1, "address", "서울")
        print(person1.address)
