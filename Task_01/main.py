# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трёхзначное число: -> '))

number1 = number % 10 
number2 = number // 100
number3 = (number % 100) // 10 
summ = number1 + number2 + number3
print(summ)