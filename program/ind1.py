#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Используя замыкания функций, объявите внутреннюю функцию, которая принимает
# в качестве аргумента список целых чисел и удаляет из него все четные или
# нечетные значения в зависимости от значения параметра type . Если type
# равен «even», то удаляются четные значения, иначе – нечетные. По умолчанию
# type должно принимать значение «even». Вызовите внутреннюю функцию замыкания
# и отобразите на экране результат ее работы.

from delete import del_items


if __name__ == "__main__":
    start_items = [0, 1, 2, 3, 4, 5, 23, 21, 14, 72]
    print(f"\n{start_items=}\n")

    del_even = del_items()
    print(f"{del_even(start_items)=}\n")

    del_not_even = del_items('not even')
    print(f"{del_not_even(start_items)=}\n")
