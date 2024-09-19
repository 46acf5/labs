
print(bool(0))

a, b, c = 3.14, 5.6, 13
print(a,b,c)

x = int(input('введите число: '))
print(x)

x = str(input('введите слово: ').ljust(5))
print(x*4)

day, month, year = int(input("день: ")), int(input("месяц: ")), int(input("год: "))
print(f"Сегодня {day}.{month}.{year}. ", end = "Всего хорошего!")

txt = 'Hello World'
print(txt[:6] + "my" + txt[5:])

print(len('Hello World'))

print('HELLO WORLD'.lower())

print('hello world'[0].upper() + 'hello world'[1:].lower().replace('o', 'O'))

n=int(input('введите число: '))
n2 = 0

while n > 0:
    digit = n % 10
    n //= 10
    n2 *= 10
    n2 += digit

print('Обратное число: ', n2)
