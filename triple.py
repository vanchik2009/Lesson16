import random

numbers = []
for i in range(10):
    numbers.append(random.randint(a = 0, b = 100))
print(numbers)







if 13 in numbers:
    print('Число 13 есть в нашем списке')
else:
    print('Числа 13 нет в нашем списке')

result = None
if 4 in numbers:
    result = 'Есть китайское несчастливое число'
else:
    result = 'Все окей'
print('Число 13 есть в нашем списке' if 13 in numbers else 'Чисола 13 нет в нашем списке')