# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = int(input("Введите положительное число максимально до 100 000: "))
message = "Число простое"

if 0 < number <= 100000:
    if number == 1 or number == 2:
        message = "Число простое"
    elif number > 2:
        for i in range(2, number):
            if number % i == 0:
                message = "Число составное"
                break
else:
    message = "Число не в указанном диапазоне"

print(message)