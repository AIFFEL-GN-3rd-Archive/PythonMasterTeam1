import math
import square2
from square2 import base, square

print(math.pi)
print(math.sqrt(4.0))
print(math.sqrt(2.0))

# 내가만든 모듈
print(base)
print(square(10))

maria = square2.Person('마리아', 20, '서울시 서초구 반포동');
print(maria.greeting())
