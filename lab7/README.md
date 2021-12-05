# Лабораторная работа №7
## Задачи
Все задачи находятся [здесь](https://informatics.msk.ru/course/view.php?id=5#section-2 "здесь")

Все задачи выполнены путем использования рекурсии

##### Задачи:
1. [Получить из 1 число N](https://informatics.msk.ru/mod/statements/view.php?id=26735#1 "Получить из 1 число N")
2. [N-е число Фибоначчи](https://informatics.msk.ru/mod/statements/view.php?id=253#1 "N-е число Фибоначчи")
3. [НОД](https://informatics.msk.ru/mod/statements/view.php?id=253&chapterid=154#1 "НОД")
4. [Ханойские башни](https://informatics.msk.ru/mod/statements/view.php?id=2550#1 "Ханойские башни")
5. [Ремонт в Ханое](https://informatics.msk.ru/mod/statements/view.php?id=2550&chapterid=3051#1 "Ремонт в Ханое")
6. [Циклические башни](https://informatics.msk.ru/mod/statements/view.php?id=2550&chapterid=3052#1 "Циклические башни")


------------
# Контрольные вопросы

**1. Что такое рекурсивная подпрограмма?**

Рекурсивная подпрограмма - это подпрограмма, которая обращается сама к себе.

**2. Что такое итерация?**

Итерация - это многократное повторение цикла.

**3. Что такое стек? Каким образом стек используется при реализации рекурсии?**
Стек - хранилище данных, при котором данные заносятся с "одной стороны", а используются с "другой стороны". В пример можно привести посуду. Чтобы взять 2 чашку нужно убрать 1.

Примером стека также можно приветси рекурсивную функцию, где каждый вызов устанавливается поверх прошлого, а завершают выполнение с последнего.

**4. Составьте рекурсивный и итерационный алгоритмы нахождения N!**

Рекурсивный:

```python
def factorial_1(n):
    if n <= 1:
        return 1
    return factorial(n - 1) * n
```

Итерационный:

```python
def factorial_2(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
```

**5. Объясните термин "косвенная рекурсия"?**

Косвенная рекурсия - это способ выполнения функции, при котором обе функции вызывают друг-друга.
