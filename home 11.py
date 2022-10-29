# При помощи функции filter() из списка слов отфильтровать только те,
# которые являются полиндромами (читаются одинаково в обе стороны),
# регистр букв не учитывать.

result = filter(lambda x: str(x[::-1]) == str(x), ['cара', 'ара', 'кок', 'нют'])
print(list(result))