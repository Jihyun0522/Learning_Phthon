# exercise.py
# Chapter02 연습문제
print('Q1')
print('=' * 30)
a = 80
b = 75
c = 55
avg = (a + b + c) / 3
print("평균 점수")
print(avg)
print('\n')

print('Q2')
print('=' * 30)
print('홀수 짝수 판별하기 ==> n % 2를 하여 1이 나오면 홀수, 0이 나오면 짝수.')
print(1)
print('1 % 2')
print(1 % 2)
print('=' * 30)
print(4)
print('4 % 2')
print(4 % 2)
print('=' * 30)
print(13)
print('13 % 2')
print(13 % 2)
print('\n')

print('Q3')
print('=' * 30)
print("pin = '881120-1068234'")
pin = '881120-1068234'
print('=' * 30)
yyyymmdd = pin[:6]
print('yyyymmdd')
print(yyyymmdd)
print('=' * 30)
num =  pin[7:]
print('num')
print(num)
print('\n')

print('Q4')
print('=' * 30)
print("pin = '881120-1068234'")
pin = '881120-1068234'
print('=' * 30)
gender = pin[7:8]
print('gender')
print(gender)
print('\n')

print('Q5')
print('=' * 30)
a = "a:b:c:d"
print(a)
print('=' * 30)
b = a.replace(':', '#')
print("b = a.replace(':', '#')")
print(b)
print('\n')

print('Q6')
print('=' * 30)
a = [1, 3, 5, 4, 2]
print(a)
print('=' * 30)
print("a.sort()")
a.sort()
print(a)
print('=' * 30)
print("a.reverse()")
a.reverse()
print(a)
print('\n')

print('Q7')
print('=' * 30)
a = ['Life', 'is', 'too', 'short']
print(a)
print('=' * 30)
print("result = ' '.join(a)")
result = ' '.join(a)
print(result)
print('\n')

print('Q8')
print('=' * 30)
a = (1, 2, 3)
print(a)
print('=' * 30)
print("a = a + (4,)")
a = a + (4,)
print(a)
print('\n')

print('Q9')
print('=' * 30)
a = dict()
print(a)
print('=' * 30)
print('다음 중 에러가 나는 것은?')
print("1. a['name'] = 'Python'")
print("2. a[('a', )] = 'Python'")
print("3. a[[1]] = 'Python'")
print("4. a[250] = 'Python'")
print('=' * 30)
print("정답은 3번")
print('딕셔너리의 key 값은 변하면 안되는데 3번의 key는 list로 변할 수 있기 때문에.')
print('\n')

print('Q10')
print('=' * 30)
a = { 'A':90, 'B':80, 'C':60 }
print(a)
print('=' * 30)
print("result = a.pop('B')")
result = a.pop('B')
print(result)
print('=' * 30)
print(a)
print('\n')

print('Q11')
print('=' * 30)
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(a)
print('=' * 30)
print("aSet = set(a)")
aSet = set(a)
print(aSet)
print('=' * 30)
print("b = list(aSet)")
b = list(aSet)
print(b)
print('\n')

print('Q12')
print('=' * 30)
print("a = b = [1, 2, 3]")
a = b = [1, 2, 3]
print(a)
print(b)
print('a is b')
print(a is b)
print('=' * 30)
print("a[1] = 4")
a[1] = 4
print(a)
print(b)
print('a is b')
print(a is b)
print('=' * 30)
print('a와 b는 동일한 [1, 2, 3]이라는 리스트 객체를 가리키고 있어 동일한 값이 출력된다.')
print('\n')
