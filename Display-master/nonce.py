import string
import random

LENGTH = 12 # 12자리

# 숫자 + 대소문자
string_pool = string.ascii_letters + string.digits

# 랜덤한 문자열 생성
result = "" 
for i in range(LENGTH) :
    result += random.choice(string_pool) # 랜덤한 문자열 하나 선택
print(result)