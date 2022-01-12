base = 2  # 변수


def square(n):  # 함수
    return base ** n


class Person:  # 클래스
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))