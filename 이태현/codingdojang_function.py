def hello():
    print('hello world!')


hello()


def add(num1, num2):
    """
    파라미터를 더해서 반환하는 함수입니다.
    :param num1: :param num2:
    :return: num1 + num2
    """
    return num1 + num2


print(add(1, 2))
print(add.__doc__)


def add_sub(num1, num2):
    return num1 + num2, num1 - num2


print(add_sub(1, 2))


def parameter(param1, param2):
    print(param1)
    print(param2)


print("위치인자")
parameter(1, 2)
print("키워드인자")
parameter(param2=2, param1=1)

x = [1, 2, 3]
print(*x)


def variable_argument(*nums):
    for num in nums:
        print(num)


variable_argument(1, 2, 3, 4, 5)


def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
personal_info(name='길동홍', age=30)


def hello(count):
    if count == 0:
        return

    print("Hello World", count)

    count -= 1
    hello(count)


hello(5)


# 회문 판별하기
def is_palindrome(word):
    if len(word) < 2:
        return
    if word[0] != word[-1]:
        return False

    return is_palindrome(word[1:-1])

