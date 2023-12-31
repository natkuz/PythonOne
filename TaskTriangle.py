# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a, b, c = int(input("Введите длину а: ")), int(input("Введите длину b: ")), int(input("Введите длину c: "))
message = None

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        message = "Треугольник равносторонний"
    elif a == b or a == c or b == c:
        message = "Треугольник равнобедренный"
    else:
        message = "Треугольник разносторонний"
else:
    message = "Треугольника с такими сторонами не существует"

print(message)