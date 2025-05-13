## Описание
Данный проект содержит решение тестового задания для Яндекс
https://practicum-for-students.yonote.ru/share/1bbf4ba8-b941-4965-ba21-1a8c1d24fac4/doc/untitled-1UnkOsqiXq

- В папке delivery: программа для подсчета стоимости доставки.
- В папке test: автотесты.
- В папке Questions: ответы на вопросы.

## Установка

1. Если в вашей системе не установлен утилита `uv`, установите ее в систему
по ссылке https://docs.astral.sh/uv/getting-started/installation/
2. Выполните установку и настройку окружения
   2.1 перейдите в директорию проекта `cd calculate`
   2.2 выполните команду `uv sync`

## Запуск тестов
для запуска тестов используйте команду
`uv run pytest -v`


## Генерация тестовых данных для pairwise

Данный метод позволяет проверить за малое количество тестов 
большую часть функциональности путем комбинации пар для различных параметров

1. Выполните команду
`uv run generate_pairwise_test_data.py`
2. Примерный вывод команды
```
====================
[[1, True, 'high', 'large'],
 [5, False, 'medium', 'large'],
 [25, False, 'low', 'small'],
 [25, True, 'medium', 'small'],
 [5, True, 'low', 'large'],
 [1, False, 'high', 'small'],
 [1, False, 'low', 'small'],
 [5, False, 'high', 'small'],
 [25, False, 'high', 'large'],
 [1, False, 'medium', 'small']]
====================
```
3. Данный массив может быть использован для тестов.
4. Пример тестирования в файле `tests/test_calculate_price.py`
