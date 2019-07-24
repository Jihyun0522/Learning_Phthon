#Exam0724
# 2-5. 딕셔너리 자료
# 딕셔너리? {key1:value1, key2:value2 ....}
dic = {'name':'pey', 'phone':'010522', 'birth':'0324'}
print(dic)

a = {'a':[1,2,3]}
print(a['a'])
print('\n')

# 딕셔너리 쌍 추가, 삭제하기
# 1. 딕셔너리 쌍 추가하기
a = {1:'a'}
print(a)
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)
print('\n')

# 2. 딕셔너리 요소 삭제하기
del a[1]
print(a)
print('\n')

# 딕셔너리를 사용하는 방법
# 딕셔너리에서 key 사용해 value 얻기
grade = {'pey':10, 'julliet':99}
print(grade)
print(grade['pey'])
print(grade['julliet'])
print('\n')

# 딕셔너리 만들 때 주의할 사항
a = {1:'a', 1:'b'}
print(a) # key가 중복되서 앞의 값은 무시됨.
#a = {[1,2]:'hi'} #형 오류 발생. 리스트는 값이 변할 수 있기 때문에 key로 사용이 불가하다.
print('\n')

# 딕셔너리 관련 함수
# key 리스트 만들기(keys)
a = {'name':'pey', 'phone':'010522', 'birth':'0324'}
print(a)
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))
print('\n')

# value 리스트 만들기(values)
print(a.values())
print('\n')

# key, value 쌍 얻기(items)
print(a.items())
print('\n')

# key:value 쌍 모두 지우기(clear)
a.clear()
print(a)
print('\n')

# key로 value 얻기(get)
a = {'name':'pey', 'phone':'010522', 'birth':'0324'}
print(a)
print(a.get('name'))
print(a.get('phone'))
print(a.get('mokey'))
print(a.get('foo','bar'))
print('\n')

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
print("'name' in a")
print('name' in a)
print("'email' in a")
print('email' in a)
print('\n')

# 2-6. 집합 자료형
# 집합 자료형? (set)
s1 = set([1, 2, 3])
print(s1)
print('\n')

# 집합 자료형의 특징
# 중복을 허용하지 않고, 순서가 없다.(unordered)
s1 = set([1, 2, 3])
print(s1)
li = list(s1) #리스트로 변환
print("'list'로 변환")
print(li)
print(li[0])
t1 = tuple(s1) #튜플로 변환
print("'tuple'로 변환")
print(t1)
print(t1[0])
print('\n')

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1)
print(s2)
print('\n')

# 교집합
print('교집합')
print(s1 & s2)
print(s1.intersection(s2))
print(s2.intersection(s1))
print('=' * 50)

# 합집합
print('합집합')
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))
print('=' * 50)

# 차집합
print('차집합')
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))
print('\n')

# 집합 자료형 관련 함수
# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
print('add')
print(s1)
s1.add(4)
print(s1)
print('\n')

# 값 여러 개 추가하기(update)
s1 = set([1, 2, 3])
print('update')
print(s1)
s1.update([4, 5, 6])
print(s1)
print('\n')

# 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
print('remove')
print(s1)
s1.remove(2)
print(s1)
print('\n')

# 2-7. 불 자료형
# 불 자료형? True, False
a = True
b = False
print(a)
print(type(a))
print('=' * 50)
print(b)
print(type(b))
print('=' * 50)
print('1 == 1')
print(1 == 1)
print('=' * 50)
print('2 > 1')
print(2 > 1)
print('=' * 50)
print('2 < 1')
print(2 < 1)
print('\n')

# 자료형의 참과 거짓
print('자료형의 참과 거짓')
print("=" * 50)
print('문자형')
print("'Python' ==> True")
print("'' ==> False")
print("=" * 50)
print('리스트')
print("[1, 2, 3] ==> True")
print("[] ==> False")
print("=" * 50)
print('튜플')
print("() ==> False")
print("=" * 50)
print('딕셔너리')
print("{} ==> False")
print("=" * 50)
print('숫자형')
print("0이 아닌 숫자 ==> True")
print("0 ==> False")
print("=" * 50)
print("None ==> False")
print('\n')

if []:
    print('True')
else:
    print('False')
print('\n')

if [1, 2, 3]:
    print('True')
else:
    print('False')
print('\n')

# 불 연산
a = 'Python'
b = ''
print(a)
print(bool(a))
print(b)
print(bool(b))

print('[1, 2, 3]')
print(bool([1, 2, 3]))

print('[]')
print(bool([]))

print(0)
print(bool(0))

print(3)
print(bool(3))
print('\n')

# 2-8. 자료형의 값을 저장하는 공간, 변수
print("'변수' = '변수에 저장할 값'")
print('\n')

# 변수란?
a = [1, 2, 3]
print(a)
print(id(a))
print('\n')

# 리스트를 복사할 때
c = [1, 2, 3]
d = c
print(c)
print(id(c))
print(d)
print(id(d))
print('c is d')
print(c is d)
c[1] = 4
print(c)
print(d)

print('=' * 50)
print('\n')

# 1. [:] 사용
print('[:] 사용')
a = [1, 2, 3]
print(a)
b = a[:]
print(' b = a[:] ')
print(b)
a[1] = 4
print(a)
print(b)
print('a is b')
print(a is b)
print('\n')

# 2. copy 모듈 사용
print('copy 모듈 사용')
from copy import copy
print('from copy import copy')
a = [1, 2, 3]
print(a)
print('b = copy(a)')
b = copy(a)
print(b)
print('a is b')
print(a is b)
print('\n')

# 변수를 만드는 여러 가지 방법
a, b = ('Python', 'life')
print("a, b = ('Python', 'life')")
print(a)
print(b)
print('=' * 50)
(a, b) = 'Phthon', 'life'
print("(a, b) = 'Phthon', 'life'")
print(a)
print(b)
print('=' * 50)
[a, b] = ['Phthon', 'life']
print("[a, b] = ['Phthon', 'life']")
print(a)
print(b)
print('=' * 50)
a = b = 'Python'
print("a = b = 'Python'")
print(a)
print(b)
print('\n')

print('변수 바꾸기')
a = 3
b = 5
print(a)
print(b)
print('a, b = b, a') # a와 b의 값을 바꿈.
a, b = b, a
print(a)
print(b)
print('\n')

# 나 혼자 코딩
a = [1, 2, 3]
b = [1, 2, 3]
print(' a = [1, 2, 3] ')
print(' b = [1, 2, 3] ')
print(a)
print(b)
print('a is b') # False
print(a is b)
print('\n')
