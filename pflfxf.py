# уровень C
#задание №1
# выбарал это решение,потому-что оно выполняет задание и я не знаю других решений
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_odd_elem():
    global numbers

    odd_sum = sum(x for x in numbers if x % 2 != 0)


    numbers = [odd_sum if x % 2 != 0 else x for x in numbers]


sum_odd_elem()
print(numbers)










#задание №2
#ищем длинну отрезка
#это решение вроде-бы правельное,у меня оно работает,оно первое был сделано
cor1=int(input("первая координата"))
cor2=int(input("вторая координата"))
num1=cor2 - cor1
if cor2 - cor1 < 0:
    print(num1-num1-num1)
else:
     print(num1)


 #ищем периметр треугольника
 #это решение рабочие,и я не знаю другов
cortr1=int(input("первая координата"))
cortr2=int(input("вторая координата"))
cortr3=int(input("третья координата"))
side1= cortr1-cortr2
if cortr1-cortr2 < 0:
    print(side1-side1-side1,"-длинна первой стороны")
else:
     print(side1,"-длинна первой стороны")

side3=cortr3-cortr1
if cortr3-cortr2 < 0:
    print(side3-side3-side3,"-длинна второй стороны")
else:
     print(side3,"-длинна второй стороны")

side2=cortr3-cortr2
if cortr3-cortr2 < 0:
    print(side2-side2-side2,"-длинна третьей стороны")
else:
     print(side2,"-длинна третьей стороны")




#задание №3
#ну это решение просто прекрасно
def is_pow_two(n):

    if n == 1:
        return True
    elif n < 1:
        return False
    else:
        return is_pow_two(n / 2)

N = int(input("напиши натуральное число N: "))

if is_pow_two(N):
    print("YES")
else:
    print("NO")