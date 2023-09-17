"""
Вариант 4:
Дан одномерный массив. Сформировать все возможные варианты данного массива путем замены отрицательных элементов на нечетных местах модулями.

Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной
реализации (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую
графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.

Ограничение: максимальная сумма элементов массива не должна превышать некоторое число .
Целевая функция: вывести массив с максимальной  суммой элементов , не превышая данное ограничение."""

import itertools
import copy
from random import randint
import tkinter as tk

from tkinter import messagebox

class Array:
    def __init__(self, n,max_sum):
        if n <= 0:
            raise ValueError("Размер массива должен быть больше 0")

        self.n = n

        self.max_sum = max_sum
        self.arr = self.generate_array()

    def generate_array(self):
        arr = [0] * self.n
        for i in range(self.n):
            arr[i] = randint(-100, 0)
        return arr

    def variants(self):
        if self.max_sum < sum(x for x in self.arr if x > 0):
            raise ValueError("Максимальная сумма не может быть меньше суммы положительных элементов")

        variants = []
        negative_indices = [i for i in range(0, len(self.arr), 2) if self.arr[i] < 0]

        for i in range(len(negative_indices) + 1):
            for combination in itertools.combinations(negative_indices, i):
                variant = copy.deepcopy(self.arr)
                for index in combination:
                    variant[index] = abs(variant[index])

                # Проверка на соответствие максимальной сумме
                if sum(variant) <= self.max_sum:
                    print(f"Полученный вариант: {variant}, сумма элементов: {sum(variant)}")
                    variants.append(variant)

        # Находим вариант с максимальной суммой элементов
        best_variant = max(variants[::-1], key=sum)
        return best_variant

def  get_values():
    try:
        n = int(entry_n.get())
        max_sum = int(entry_max_sum.get())

        array_manipulator = Array(n, max_sum)
        best_variant = array_manipulator.variants()
        label_array.configure(text=f"Изначальный массив:\n{array_manipulator.arr}")
        label_output.configure(text=f"Массив с максимальной суммой элементов:\n{best_variant}")


    except ValueError as e:
         messagebox.showerror("Ошибка", str(e))
window = tk.Tk()
label_n = tk.Label(window, text="Введите размер массива:")
label_n.pack()
entry_n = tk.Entry(window)
entry_n.pack()

label_max_sum = tk.Label(window, text="Введите максимальную сумму:")
label_max_sum.pack()
entry_max_sum = tk.Entry(window)
entry_max_sum.pack()

# Создаем кнопку для подтверждения ввода
button = tk.Button(window, text="Ввод", command=get_values)
button.pack()
label_array = tk.Label(window, text="")
label_array.pack()
# Создаем метку для вывода результата
label_output = tk.Label(window, text="")
label_output.pack()
window.mainloop()


