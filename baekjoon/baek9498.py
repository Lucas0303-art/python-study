# 시험 점수를 입력받아 
# 90 ~ 100점은 A, 
# 80 ~ 89점은 B, 
# 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 
#  input : 95
# output: A
# input : 87
# output : B
# input : 42
# output: F
a = int(input('type in number'))
if a>90:
    print('a')

elif a>80:
    print('b')
elif a>70:
    print('c')
elif a>60:
    print('d')
else:
    print('f')