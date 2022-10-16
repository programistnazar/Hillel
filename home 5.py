# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for
n = int(input())
q = 1
result = 0
while q <= n:
    if not q % 3 == 0:
        result += q ** 3
    q += 1
print(result)

num_sum = 0
for b in range(1, n+1):
    if not b % 3 == 0:
        num_sum += b ** 3
print(num_sum)
