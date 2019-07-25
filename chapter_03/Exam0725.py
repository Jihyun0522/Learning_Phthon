# Exam0725.py
# 3장 프로그램의 구조를 쌓는다! 제어문
# 3-1. if문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if문의 기본 구조
print("if문의 기본 구조")
print("if 조건문:")
print("\t수행할 문장 1...")
print("else:")
print("\t수행할 문장 A...")
print('=' * 30)
print('반드시 if 조건문: 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기를 해야한다.')
print('들여쓰기는 공백(SpaceBar) 또는 탭(Tab) 중 하나로 통일하는 것이 좋다.')
print('\n')

# 조건문이란 무엇인가?
print("'조건문'이란 참과 거짓을 판단하는 문장")
print('=' * 30)

# 비교 연산자
print('비교 연산자')
print('x < y : x가 y보다 작다')
print('x > y : x가 y보다 크다')
print('x == y : x가 y와 같다')
print('x != y : x가 y와 같지 않다')
print('x >= y : x가 y보다 크거나 같다')
print('x <= y : x가 y보다 작거나 같다')
print('=' * 30)
x = 3
y = 2
print(x)
print(y)
print('x > y')
print(x > y)
print('x < y')
print(x < y)
print('x == y')
print(x == y)
print('x != y')
print(x != y)
print('=' * 30)
money = 2000
print(money)
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print('=' * 30)

# and, or, not
print('and, or, not')
print('x and y : x와 y 둘 중에 하나만 참이면 참이다.')
print('x or y : x와 y 모두 참이어야 참이다.')
print('not y : y가 거짓이면 참이다.')
print('=' * 30)
card = True
if money >= 3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
print('=' * 30)

# in s, x not in s
print('in s, x not in s')
print('x in 리스트 <-> x not in 리스트')
print('x in 튜플 <-> x not in 튜플')
print('x in 문자열 <-> x not in 문자열')
print('=' * 30)
print('1 in [1, 2, 3]')
print(1 in [1, 2, 3])
print('1 not in [1, 2, 3]')
print(1 not in [1, 2, 3])
print("'a' in ('a', 'b', 'c')")
print('a' in ('a', 'b', 'c'))
print("'a' not in ('a', 'b', 'c')")
print('a' not in ('a', 'b', 'c'))
print('=' * 30)
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어가라')
print('\n')

# 나 혼자 코딩
print('주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라')
pocket = ['paper', 'cellphone', 'money', 'card']
print(pocket)
if 'card' in pocket:
    print('버스를 타고 가라')
else:
    print('걸어 가라')
print('\n')

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
print("if 조건문:")
print("\tpass")
print("else:")
print("\t수행할 문장 A...")
print('=' * 30)
print('pass을 이용하면 아무 결괏값도 보여주지 않는다.')
print('\n')

# 다양한 조건을 판단하는 elif
print('다양한 조건을 판단하는 elif')
print('=' * 30)
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print('택시를 타고 가라')
    else:
        print('걸어 가라')
print('=' * 30)
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
print('=' * 30)
print('elif는 이전 조건문이 거짓일 때 수행된다.')
print('=' * 30)
print("if문의 기본 구조")
print("if 조건문:")
print("\t수행할 문장 1-1...")
print("elif 조건문2")
print("\t수행할 문장 2-1...")
print("elif 조건문N")
print("\t수행할 문장 N-1...")
print("else:")
print("\t수행할 문장 A...")
print('개수에 제한 없이 elif를 사용할 수 있다.')
print('\n')

# 조건부 표현식
print('조건부 표현식')
print('조건문이 참일 경우 if 조건문 else 조건문이 거짓일 경우')
print('=' * 30)
print("ex) message = 'success' if score >= 60 else 'failure'")
print('=' * 30)
print('가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.')
print('\n')

# 3-2. while문
# while문의 기본 구조
print('while문의 기본 구조')
print('while 조건문:')
print("\t수행할 문장 1")
print("\t수행할 문장 2")
print("\t수행할 문장 3")
print('=' * 30)
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' %treeHit)
    if treeHit == 10:
        print('나무가 넘어갑니다.')
print('\n')

# while문 만들기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
print(prompt)
number = 0
while number != 4:
    print(prompt)
    number = int(input())
print('\n')

# while문 강제로 빠져나가기
print('while문 강제로 빠져나가기')
print("'break'를 사용하는 것.")
print('=' * 30)
coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee - 1
    print('남은 커피의 양은 %d개입니다.' %coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break
print('\n')

print('=' * 30)
# coffee

coffee = 2
while True:
    money = int(input('돈을 넣어주세요 : '))
    if money == 300:
        print('커피를 줍니다.')
        coffee = coffee - 1
    elif money > 300:
        print('거스름돈 %d원을 주고 커피를 줍니다.' %(money - 300))
        coffee = coffee - 1
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.')
        print('남은 커피의 양은 %d개입니다.' %coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break
    print('\n')
    
# coffee
print('\n')

# while문의 맨 처음으로 돌아가기
print('while문의 맨 처음으로 돌아가기')
print('continue를 사용하면 while문의 맨 처음으로 돌아간다.')
print('=' * 30)
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
print('\n')

# 무한 루프
#while True:
#    print("'Ctrl + C'를 눌러야 while문을 빠져나갈 수 있습니다.")
print('무한 루프란 무한히 반복한다는 의미')
print('while True:')
print('\t수행할 문장1 ...')
print("'Ctrl + C'를 눌러야 while문을 빠져나갈 수 있습니다.")
print('\n')

# 3-3. for문
#for문의 기본 구조
print('for문의 기본 구조')
print('for 변수 in 리스트 또는 튜플 또는 문자열:')
print('\t수행할 문장1')
print('=' * 30)

# 1. 전형적인 for문
print('1. 전형적인 for문')
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
print('=' * 30)

# 2. 다양한 for문의 사용
print('2. 다양한 for문의 사용')
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
print('=' * 30)

# 3. for문의 응용
print('3. for문의 응용')
# marks1

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

# marks1
print('\n')

# for문과 continue문
print('for문과 continue문')
# marks2

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    else:
        print("%d번 학생 합격입니다. 축하합니다." %number)

# marks2
print('while문처럼 for문에서도 continue를 사용하여 for문의 처음으로 돌아간다.')
print('\n')

# for문과 함께 자주 사용하는 range 함수
print('for문과 함께 자주 사용하는 range 함수')
print('a = range(10)')
a = range(10)
print(a)
print('range(10)은 0부터 10미만의 숫자를 포함하는 range 객체를 만들어 준다.')
print('range(시작 숫자, 끝 숫자)의 형태를 사용하는데, 이 때 끝 숫자는 포함되지 않는다.')
print('=' * 30)

# range 함수의 예시 살펴보기
print('range 함수의 예시 살펴보기')
add = 0
for i in range(1, 11):
    add = add + i
print(add)
print('=' * 30)

# marks3

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))

# marks3
print('=' * 30)

# for와 range를 사용한 구구단
print('for와 range를 사용한 구구단')
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print(' ')
print('\n')

# 리스트 내포 사용하기
print('리스트 내포 사용하기')
a = [1, 2, 3, 4]
print(a)
result = []
for num in a:
    result.append(num * 3)
print(result)
print('=' * 30)

a = [1, 2, 3, 4]
print(a)
result = [num * 3 for num in a]
print(result)
print('=' * 30)

a = [1, 2, 3, 4]
print(a)
result = [num * 3 for num in a if num % 2 == 0]
print(result)
print('=' * 30)

print('리스트 내포의 일반 문법')
print('[표현식 for 항목 in 반복 가능 객체 if 조건]')
print('=' * 30)

print('for문을 2개 이상 사용하는 것도 가능')
print('[표현식 for 항목1 in 반복 가능 객체 if 조건1\n\t...\n\tfor 항목n in 반복 가능 객체 if 조건n]')
print('\n')
