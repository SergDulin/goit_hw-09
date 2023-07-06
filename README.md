# Домашнє завдання

GOIT > Курс > Python Developer > Python core > Модуль 9. Функції (декоратори, замикання)

# Додаток Телефонна книга


Це простий командний рядковий додаток для телефонної книги, реалізований на Python. Він дозволяє додавати контакти, змінювати їх номери телефонів, отримувати номери телефонів за іменем і відображати всі контакти.

## Використання

Додаток підтримує наступні команди:

- `hello`: Виводить привітальне повідомлення.
- `add [name] [phone]`: Додає контакт з вказаним іменем та номером телефону.
- `change [name] [phone]`: Змінює номер телефону існуючого контакту з вказаним іменем.
- `phone [name]`: Отримує номер телефону контакту за іменем.
- `show all`: Відображає всі контакти в телефонній книзі.
- `good`, `bye`, `close`, `exit`: Виходить з додатку.

## Опис роботи

Цей код реалізує простий зберігач контактів з можливістю додавання, зміни та отримання номерів телефонів контактів, а також виведення всіх контактів. Він також має базовий інтерфейс командного рядка для взаємодії з користувачем.

## Особливості роботи

Ім'я може бути с кілька слов, неохідно мінімум одно. При пошуку чи зміні телефона, можно вводити ім'я любим регістром. Команда "show all" виводить імена з великої літери. При пошуку телефона достатньо одного імені, команда "phone" виводить список телефонов в яких є таке ім'я. 

