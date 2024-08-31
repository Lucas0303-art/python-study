# 문제: 간단한 계산기 만들기
# 두 개의 숫자와 하나의 연산자를 입력받아, 해당 연산을 수행하는 프로그램을 작성하세요.
# 지원할 연산자는 +, -, *, / 네 가지입니다.
# 사용자가 잘못된 연산자를 입력한 경우 "잘못된 연산자입니다." 라고 출력하세요.

# 예시 입력:
# 첫 번째 숫자: 10
# 연산자: *
# 두 번째 숫자: 5

# 예시 출력:
# 결과: 50
# a = "5"
# b=5
# operator="+"
# if operator="+1"


# input two number one operator
# two number 
a=6 # input
b=10 # input 
# one operator
operator = "/"

# +,-,*,/,check
# + check
if operator=="+":
    # + 연산 
    print("result=",a+b)
# - check
elif operator=="-":
    # - 연산
    print("result=",a-b)
# * check
elif operator=="*":
    # * 연산
    print("reult=",a*b)
# / check
elif operator=="/":
    # /연산
    print("result=",a/b)
# wrong operator 