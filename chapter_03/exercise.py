# exercise.py
# Chapter03 연습문제
print('Q1')
print('=' * 30)
a = 'Life is too short, You need python'
print(a)

if 'wife' in a: print('wife')
elif 'Python' in a and 'you' not in a: print('Python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')
print('\n')

print('Q2')
print('=' * 30)
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)
print('\n')

print('Q3')
print('=' * 30)
i = 0

while True:
    i += 1
    if i > 5: break
    print('*' * i)
print('\n')

print('Q4')
print('=' * 30)
for i in range(1, 101):
    print(i)
print('\n')

print('Q5')
print('=' * 30)
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score
average = total / len(A)
print(average)
print('\n')

print('Q6')
print('=' * 30)
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)
print('=' * 20)

result = []
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
print('\n')
