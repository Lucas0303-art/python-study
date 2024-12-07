# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# input : 10 20
# output : <
# input : 15 10
# output : >
# input : 10 10
# output : =

a = int(input('type in number'))
b = int(input('type in number'))

if a>b:
    print('>')

elif a<b:
    print('<')

elif a==b:
    print('=')
