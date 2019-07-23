# Exam0723.py
# 2-1. 숫자형
print("숫자형")
a = 123
print(a)

a = 1.2
print(a)

a = 4.24E10 #42400000000.0
print(a)

a = 4.24e-10
print(a)

a = 0o177 #127
print(a)

a = 0x8ff #2303
print(a)

a = 0xabc #2748
print(a)
print('\n')

a = 3
b = 4
print(a + b)
print(a * b)
print(a / b)
print('\n')

print(a ** b) # **는 제곱을 나타내는 연산자
print('\n')

print(7 % 3)
print('\n')

print(7 // 4) # //는 몫 중 정수값만 돌려줌.
print('\n')

# 2-2. 문자열 자료형
print("문자열 자료형")
# 문자열 만드는 방법
# 1. ""로 둘러싸기
print("Hello World!")
print('\n')

# 2. ''로 둘러싸기
print('Python is fun!')
print('\n')

# 3. """ """로 둘러싸기
print("""Life is too short, You need Python""")
print('\n')

# 4. ''' '''로 둘러싸기
print('''Life is too short, You need Python''')
print('\n')

# 문자열 안에 작은따옴표나 큰 따옴표 추가 시키기

# 1. 문자열에 ' 포함시키기
food = "Python's favorite food is perl"
print(food)
#food = 'Python's favorite food is perl'
# 위의 문장은 '가 3개 있어 에러가 남.
print('\n')

# 2. 문자열에 " 포함시키기
say = '"Python is very easy" he says'
print(say)
print('\n')

# 3. 백슬래시(\)를 사용하여 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy\" he says."

print(food)
print(say)
print('\n')

# 여러 줄인 문자열을 변수에 대입할 때
# 1. 줄을 바꾸는 '\n' 삽입
multiline = "Life is too short\nYou need Python"
print(multiline)

# 2. ''' 또는 """ 사용하기
multiline = '''
Life is too short
You need Python
'''
print(multiline)

multiline = """
Life is too short
You need Python
"""
print(multiline)

# 이스케이프 코드
# \n : 문자열 안에서 줄을 바꿀 때
# \t : 문자열 사이에 탭 간격을 주고 싶을 때
# \\ : 문자 \를 그대로 표현할 때
# \' : '를 그대로 표현할 때
# \" " "를 그대로 표현할 때
# \r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a : 벨소리
# \b : 백스페이스
# \000 : 널 문자

#문자열 연산하기

# 1. 문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = "is fan"
print(head + tail)
print('\n')

# 2. 문자열 곱하기
a = "Python"
print(a * 2)
print('\n')

# 3. 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)
print('\n')

# 4. 문자열 길이 구하기
a = "Life is too short"
print(a)
print(len(a))

b = "You need Python"
print(b)

print(len(b))
print('\n')

# 문자열 인덱싱과 슬라이싱
# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a)
print(a[3]) # life의 e
print('\n')

print(a[0])
print(a[-0])
print(a[-2]) # 뒤에서 2번째 문자
print(a[-5]) # 뒤에서 5번째 문자
print('\n')

# 문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
print(a)
print(b)
print(a[0:4])
print(a[0:3])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])
print('\n')

a = "20010522Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
print('\n')

year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)
print('\n')

a = 'Pithon'
print(a[:1] + 'y' + a[2:]) #Python
print('\n')

# 문자열 포매팅
# 1. 숫자 바로 대입
print("I eat %d apples" %3)
print('\n')

# 2. 문자열 바로 대입
print("I eat %s apples" %"five")
print('\n')

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples" %number)
print('\n')

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. So I was sick for %s days." %(number, day))
print('\n')

# 문자열 포맷 코드
# %s : 문자열(String)
# %c : 문자 1개(Character)
# %d : 정수(Integer)
# %f : 부동 소수(Floating-point)
# %o : 8진수
# %x : 10진수
# %% : %

print("I have %s apples" %3) # %s는 %뒤에 있는 값을 문자열로 바꾼다.
print('\n')

#포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백
print("%10s" %"hi")
print("%-10sjane" %"hi")
print('\n')

# 2. 소수점 표현하기
print("%0.4f" %3.1415920)
print("%10.4f" %3.141592)
print('\n')

#format 함수를 사용한 포매팅
# 숫자 바로 대입하기
print("I eat {0} apples".format(3))

# 문자열 바로 대입
print("I eat {0} apples".format("five"))

# 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))

# 2개 이상의 값 넣기
day = "five"
print("I ate {0} apples. So I was sick for {1} days.".format(number, day))

# 이름으로 넣기
print("I ate {number} apples. So I was sick for {day} days.".format(number = 4, day = 2))

# 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. So I was sick for {day} days.".format(8, day=3))

# 왼쪽 정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현하기
y = 3.141592
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# { 또는 } 문자 표현하기
print("{{ and }}".format())

# f 문자열 포매팅
name = 'Jihyun'
age = 18
print(f'내 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'내년에 {age + 1}살이 됩니다.')

d = {'name':'Jihyun', 'age':18}
print(f'내 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

print(f'{y:0.4f}')
print(f'{y:10.4f}')

print(f'{{ and }}')

print("{0:!^12}".format("Python"))
print(f'{"Python":!^12}')

print('\n')

#문자열 관련 함수
# 문자 세기 함수(count)
a = 'hobby'
print(a)
print(a.count('b'))

# 위치 알려주기 1(find)
a = "Python is the best choice"
print(a.find('b')) #문자열에서 b가 처음으로 나온 위치
print(a.find('k'))

# 위치 알려주기 2(index)
a = 'Life is too short'
print(a.index('t'))
# print(a.index('k')) # <-- k가 없어서 에러가 발생

# 문자열 삽입(join)
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기(lstrip)
a = "   hi   "
print(a)
print(a.lstrip())

# 오른쪽 공백 지우기(rstrip)
print(a.rstrip())

# 양쪽 공백 지우기(strip)
print(a.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a)
print(a.replace("Life", "Your leg"))

# 문자열 나누기(split)
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(":"))

print('\n')

# 2-3. 리스트 자료형
print("리스트 자료형")
# 리스트? []사용
a = [1, 2, 3, 4, 5]
print(a)

b = [1, 2, ["Life", "is"]]
print(b)

# 리스트의 인덱싱과 슬라이싱
# 리스트의 인덱싱
a = [1, 3, 5, 7, 9]
print(a)
print(a[0])
print(a[1] + a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a)
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])
print('\n')

# 삼중 리스트에서 인덱싱
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a)
print(a[2][2][0])
print('\n')

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a)
print(a[0:2])

b = '12345'
print(b)
print(b[0:2])

b = a[:2]
c = a[2:]
print(b)
print(c)
print('\n')

# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a)
print(a[2:5])
print(a[2][:2])
print('\n')

# 리스트 연산하기
# 1. 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a)
print(b)
print(a + b)
print(str(a[1]) + " hi")

# 2. 리스트 반복하기(*)
print(a * 3)

# 3. 리스트 길이 구하기
print(len(a))
print('\n')

# 리스트의 수정과 삭제
# 리스트에서 값 수정하기
a = [1, 2, 3]
print(a)
a[2] = 4
print(a)

# del 함수를 이용해 리스트 요소 삭제하기
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
print(a)
del a[2:]
print(a)
print('\n')

# 리스트 관련 함수
# 리스트에 요소 추가(append)
a = [1, 2, 3]
print(a)
a.append(4)
print(a)
a.append([5, 6])
print(a)
print('\n')

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
print(a)
a.sort()
print(a)

a = ['b', 'c', 'a']
print(a)
a.sort()
print(a)
print('\n')

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
print(a)
a.reverse()
print(a)
print('\n')

# 위치 반환(index)
a = [1, 2, 3]
print(a)
print(a.index(3))
print(a.index(1))
#print(a.index(0)) #리스트에 0이 존재하지 않으므로 에러가 발생
print('\n')

# 리스트에 요소 삽입(insert)
a = [1, 2, 3]
print(a)
a.insert(0, 4) # a[0]의 4번째에 삽입
print(a)
a.insert(3, 5) # a[3]의 5번째에 삽입
print(a)
print('\n')

# 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
print(a)
a.remove(3)
print(a)
a.remove(3)
print(a)
print('\n')

# 리스트 요소 끄집어내기(pop)
a = [5, 6, 7]
print(a)
a.pop()
print(a)
a.pop(0)
print(a)
print('\n')

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
print(a)
a.count(1)
print('\n')

# 리스트 확장(extend)
a = [1, 2, 3]
print(a)
a.extend([4, 5])
print(a)
b = [6, 7]
print(b)
a.extend(b)
print(a)
print('\n')

# 2-4. 튜플 자료형
print("튜플 자료형")
# 튜플? ()
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print('\n')

# 튜플의 요솟값을 지우거나 변경하려고 한다면?
# 1. 튜플의 요솟값을 삭제하려 할 떼
t1 = (1, 2, 'a', 'b')
print(t1)
#del t1[0] # 지워지지 않기 때문에 에러가 발생한다.

# 2. 튜플의 요솟값을 변경하려 할 때
#t1[0] = 'c' # 변경하는 것이 지원되지 않기 때문에 에러가 발생함.

#튜플 다루기
# 1. 인데싱하기
t1 = (1, 2, 'a', 'b')
print(t1)
print(t1[0])
print(t1[3])

# 2. 슬라이싱하기
print(t1[1:])

# 3. 튜플 더하기
t2 = (3, 4)
print(t2)
print(t1 + t2)

# 4. 튜플 곱하기
print(t2 * 3)

# 5. 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
print(t1)
print(len(t1))
print('\n')
