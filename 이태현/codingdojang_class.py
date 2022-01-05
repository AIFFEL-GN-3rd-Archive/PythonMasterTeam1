class Person:
    def greeting(self):
        print('hello')


james = Person()

james.greeting()

# init 매서드
class Person:

    def __init__(self):
        self.personinit = 'helloinit'

    def greeting(self):
        print(self.personinit)

    def hello(self):
        self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출


james = Person()
james.hello()  # Hello

# 비공개 속성
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# maria.__wallet -= 10000  # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)

# 정적 메서드
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)


Calc.add(10, 20)  # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)  # 클래스에서 바로 메서드 호출


# 클래스 메서드
class Person:
    count = 0  # 클래스 속성

    def __init__(self):
        Person.count += 1  # 인스턴스가 만들어질 때
        # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))  # cls로 클래스 속성에 접근


james = Person()
maria = Person()
you = Person()

Person.print_count()  # 3명 생성되었습니다.


# 상속
class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def study(self):
        print('공부하기')


james = Student()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Student에 추가한 study 메서드


# 상속과 포함관계
class Person:
    def greeting(self):
        print('안녕하세요.')


class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)


p = Person()
plist = PersonList()

plist.append_person(p)

## 추상 클래스
from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')


james = Student() # Student에서 go_to_school을 정의하지 않음
james.study()
james.go_to_school()
